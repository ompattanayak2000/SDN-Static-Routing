<img width="975" height="545" alt="image" src="https://github.com/user-attachments/assets/b27ffc7c-497d-4bb6-a3c1-d4c48efe9e9c" /># Static Routing using SDN Controller (Ryu + Mininet)

## 📌 Project Overview
This project demonstrates **Static Routing using Software Defined Networking (SDN)** with the **Ryu Controller** and **Mininet emulator**.

The controller installs flow rules in switches to enable communication between hosts in a predefined topology.

---

## 🎯 Problem Statement
Traditional networks use distributed control logic, making routing complex and less flexible.  
This project implements **static routing using a centralized SDN controller**, where:

- The controller manages packet forwarding decisions
- Flow rules are installed dynamically in switches
- Hosts communicate through SDN-controlled paths

---

## 🛠️ Technologies Used
- Python 3
- Ryu SDN Controller
- Mininet Network Emulator
- Open vSwitch (OVS)
- OpenFlow Protocol (v1.3)

---

## ⚙️ Setup Instructions

### 1. Install Dependencies
  sudo apt update
  sudo apt install mininet openvswitch-switch python3-pip -y
Step 2: Create Virtual Environment
  python3 -m venv ryu-env
  source ryu-env/bin/activate
Step 3: Install Ryu and Dependencies
  pip install ryu==4.34
  pip install eventlet==0.30.2
  pip install dnspython==1.16.0
Step 4: Start Ryu Controller
  (Open Terminal 1)
  cd ~
  source ryu-env/bin/activate
  export EVENTLET_NO_GREENDNS=yes
  ryu-manager ryu.app.simple_switch_13
Step 5: Run Mininet Topology
  (Open Terminal 2)
  sudo mn --topo linear,2 --controller remote
Step 6: Test Connectivity
  (In Mininet CLI)
  pingall
Step 7: Exit Mininet
  exit
Step 8: Check Flow Rules
  sudo ovs-ofctl -O OpenFlow13 dump-flows s1
  sudo ovs-ofctl -O OpenFlow13 dump-flows s2
Step 9: Regression Test
  Delete flows
  sudo ovs-ofctl del-flows s1
  sudo ovs-ofctl del-flows s2
  Restart Controller
  (Go to Terminal 1)
  CTRL + C
  ryu-manager ryu.app.simple_switch_13
  Run Mininet again
  sudo mn --topo linear,2 --controller remote
  Test again
  pingall

EXPECTED OUTPUT SCREENSHOTS


  
