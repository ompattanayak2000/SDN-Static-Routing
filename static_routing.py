from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet


class SimpleSwitch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def init_(self, *args, **kwargs):
        super(SimpleSwitch, self)._init_(*args, **kwargs)
        self.mac_to_port = {}

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        dp = msg.datapath
        ofp = dp.ofproto
        parser = dp.ofproto_parser

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)

        dpid = dp.id
        self.mac_to_port.setdefault(dpid, {})

        src = eth.src
        dst = eth.dst
        in_port = msg.match['in_port']

        self.mac_to_port[dpid][src] = in_port

        out_port = self.mac_to_port[dpid].get(dst, ofp.OFPP_FLOOD)

        actions = [parser.OFPActionOutput(out_port)]

        if out_port != ofp.OFPP_FLOOD:
            match = parser.OFPMatch(in_port=in_port, eth_dst=dst)
            mod = parser.OFPFlowMod(datapath=dp, match=match,
                                   actions=actions)

            
            dp.send_msg(mod)

        out = parser.OFPPacketOut(datapath=dp,
                                 buffer_id=msg.buffer_id,
                                 in_port=in_port,
                                 actions=actions,
                                 data=msg.data)
        dp.send_msg(out)
