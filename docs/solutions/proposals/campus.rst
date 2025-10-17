====================================================
Campus/Enterprise Network Architecture
====================================================

:Document Title:  Technical Proposal – Network Infrastructure Modernization
:Submitted By:    Alcatel-Lucent Enterprise
:Revision:        1.0


1. Executive Summary
====================

The Proposed Solution shall deliver a secure, resilient, and scalable enterprise network infrastructure
supporting wired, wireless, and hybrid-cloud connectivity.  It shall provide end-to-end high availability,
zero-trust security, and centralized visibility to meet the Authority’s/Customer **(delete appropriate)** operational and compliance objectives.

Key features include:

* Three-tier redundant **Campus LAN/WLAN**
* **EVPN Data Center** spine-leaf fabric
* **Hybrid Cloud** integration (AWS/Azure)
* **SD-WAN/Internet Edge** with dual ISPs
* **Unified Communication** and **Remote Access VPN**
* Centralized Management, identity, telemetry, and automation services


2. Scope and Objectives
=======================

The scope of this project shall encompass design, supply, installation, configuration, testing,
and commissioning of the enterprise network infrastructure, including:

* Campus switching and wireless systems
* Data-center fabric, Data Center interconnect, and Data-to-cloud connectivity
* Internet & VPN connectivity
* Unified communications integration
* Network security, access control, and monitoring
* Ongoing support, training, and documentation

**Objectives**

* Modernize the existing network to support digital-first services
* Transform the Wireless network to Wi-Fi 6/6E/7 **(delete appropriate)** technology to improve coverage and experiences.
* Enhance availability to ≥ 99.95 % uptime
* Improve performance and scalability through automation and SD-WAN
* Strengthen cybersecurity posture through segmentation, least privilege access, identity management, and MFA


3. Existing Environment
=======================

The current environment consists of legacy L2/L3 switching and independent WLAN controllers.
It lacks unified management, network policy control, dynamic routing, and centralized visibility.
Poor wireless coverage and performance to support high bandwidth applications.
Performance degradation and manual configuration have resulted in limited scalability.
The proposed modernization shall address these constraints through an integrated, modular architecture.


4. Proposed Solution Overview
=============================

The Proposed Solution shall introduce a unified, service-oriented architecture
covering access (wired and wireless), aggregation **(delete appropriate)**, core, data-center, and cloud domains.

Key Design Principles
----------------------

* High availability and fault tolerance – no single point of failure
* Modular scalability – independent growth of domains
* Standards-based interoperability (IEEE, IETF)
* Zero-Trust security and Identity management with Microsoft Entra ID **(delete appropriate)**
* End-to-end QoS policy control for different class of applications (Gold/Silver/Bronze)
* Centralized monitoring, automation, and analytics


5. Solution Architecture Principles
===================================

* **Resiliency:**  Dual control modules & fabric, redundant PSUs, Virtual Chassis, RSTP, LACP, BFD-assisted OSPF/BGP routing, and ECMP.
* **Redundancy:**  Hardware, link, and power-feed duplication across all layers.
* **Security:**  VRF/VLAN for macro segmentation, Role-based with ACL for micro-segmentation, 802.1X/MAB, and identity & MFA management.
* **Scalability:**  Horizontal expansion through stackable or leaf-spine designs.
* **Operational Efficiency:**  Single-pane-of-glass management with OmniVista 2500/Cirrus **(delete appropriate)**, Infrastructure-as-Code (IaC) deployment, API-based integration,
  and automated configuration validation.


6. Proposed Architecture and Design
===================================

6.1 High-Level Architecture Overview
------------------------------------

High-level architecture diagram

.. image:: campus_network_architecture.png
   :alt: Campus Network Architecture
   :align: center
   :width: 800px

   :height: 600px

The Proposed Solution shall comprise six (6) inter-connected network domains:

#. Campus LAN, and WLAN with Distributed WLAN Architecture
#. EVPN Data Center (Spine-Leaf Fabric)
#. Hybrid Cloud (AWS/Azure Connectivity)
#. Internet Edge and SD-WAN Perimeter
#. Unified Communication (Voice/Video/Collaboration)
#. Remote VPN / Work-from-Home Access

All components shall be engineered with redundancy at device, link, and control-plane levels,
ensuring *no single point of failure*.


6.2 Detailed Architecture by Domain
-----------------------------------

6.2.1 Campus LAN / WLAN (Three-Tier Architecture)/(Two-Tier Architecture) **(delete appropriate)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Overview**

The Campus network shall adopt a **Three-Tier Architecture**/ **Two-Tier Architecture** **(delete appropriate)** consisting of **Core**, **Distribution** **(delete appropriate)**,
and **Access** layers, each engineered for redundancy, resiliency, and deterministic convergence.

**A. Core Layer** **(please adapt for Virtual Chassis)**

* Two (2) or more high-performance core switches in redundant pair.
* Dual supervisors, fabric modules, PSUs, and hot-swappable interface cards.
* Inter-core 40/100 Gbps LACP links; ECMP routing toward Distribution.
* **OSPF + BFD** for sub-second failover; **NSF/GR** for control-plane stability.
* Dual uplinks from every Distribution pair to both Core nodes.

**B. Distribution Layer** **(please adapt for Virtual Chassis)** **(delete appropriate)**

* Redundant Distribution pairs with **Virtual Chassis** or equivalent to Access.
* Dual supervisors and PSUs per chassis.
* **MVRP** for dynamic VLAN registration.
* **RSTP/MSTP** for L2 recovery < 2s recovery.
* **HSRP/VRRP** default-gateway redundancy.
* **OSPF + BFD** uplinks to Core; inter-distribution link for sync.

**C. Access Layer**

* Stack/Virtual-Chassis access switches with ISSU support.
* **MVRP** for dynamic VLAN registration
* Dual LACP uplinks to both Distribution switches.
* 802.1X/MAB NAC enforcement; DHCP Snooping / ARP Inspection.
* Dual power feeds and PoE priority for critical devices.

**D. Wireless LAN Subsystem**

* OmniVista 2500/Cirrus centralized WLAN management. **(delete appropriate)**
* Wi-Fi 6/6E/7 **(delete appropriate)** APs with 802.11r/k/v fast roaming.
* APs powered via PoE+ switches.
* Auto RF optimization and automatic channel/power adjustment.
* L2 and L3 roaming support.
* WPA2/WPA3 personal and Enterprise security modes.
* 802.1X/MAC and RADIUS integration.
* Microsoft Entra ID **(delete appropriate)** for identity-based access control.
* Bonjour/mDNS service discovery.
* wIDS/IPS with dedicated scanning radio **(delete appropriate)**
* Rogue AP detection and containment.
* Role-based WLAN segmentation (Corp, Guest, IoT, Voice).
* L2-L7 access-control
* QoS for voice/video prioritization.
* IoT analytics and device profiling.
* Guest Management and Captive Portal support.
* Guest onboarding via self-service portal, vouchers, sponsor approval, social media login (Facebook/Google).
* BYOD onboarding
* Heatmap & Floorplan visualization.
* Client/AP analytics and reporting.


**E. Operational Resilience**

.. list-table:: 
   :header-rows: 1
   :widths: 20 40 40

   * - **Layer**
     - **Redundancy Measures**
     - **Convergence / Protection**
   * - Core
     - Dual nodes, LACP links, dual PSUs
     - OSPF + BFD + ECMP + GR/NSF
   * - Distribution
     - MLAG, dual PSUs, HSRP/VRRP
     - RSTP / MSTP
   * - Access
     - Stack/VC, dual uplinks (LACP)
     - ISSU + Edge Security + PoE Redundancy
   * - WLAN
     - Overlapped Radio coverage, Redundant management
     - 802.11r/k/v Fast Failover, wIDS/IPS Rogue AP Containment


6.2.2 EVPN Data Center (Spine/Leaf Fabric)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Data Center Fabric shall adopt a **spine-and-leaf** architecture consisting of **10/25/40/50/100 Gbe** **(delete appropriate)** spine and leaf nodes.
The Data Center shall support east-west traffic patterns, workload mobility, and multi-tenancy through VXLAN/EVPN overlays.

* Non-blocking **Spine-Leaf** topology with Layer 3 links for **ECMP** load-balancing.
* Each Leaf dual-homed to Spines; underlay OSPF for IGP with BFD for fast convergence.
* VXLAN overlay with **EVPN Multihoming (EVPN-MH)** for active-active links.
* Distributed anycast gateways for workload mobility, and optimal routing.

A pair of leaf nodes shall provide connectivity to Campus Core and Hybrid Cloud gateways.

6.2.3 Hybrid Cloud (AWS/Azure Integration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Redundant **Direct Connect / Transit Gateway** circuits/service via separate PoPs/providers.
* Segregated VRFs/VPCs for Prod/Dev/DR environments.
* BGP to OSPF redistribution for routes convergence.


6.2.4 Internet Edge and SD-WAN Perimeter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Dual firewalls (Active/Active or Standby) with state synchronization.
* Dual edge routers with dual ISPs using eBGP multi-homing.
* **SD-WAN fabric** over Internet/MPLS/5G **(delete appropriate)** underlays.
* Application-aware path selection, FEC, packet duplication.
* Dual SD-WAN controllers in HA mode / CLoud controller **(delete appropriate)**.


6.2.5 Unified Communication (Voice / Video / Collaboration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Redundant Call Manager servers.
* SBC gateway with HA for SIP trunks to telco/carriers.
* Branch Survivable Remote Gateways for WAN failover.
* QoS: EF (RTP), AF41 (Video), CS3 (Signaling).
* SRTP and TLS for media and signaling encryption.
* IP Phones (wired/Wi-Fi/Dect) auto-provisioning via TFTP/HTTP(S).
* Unified Communications service such as presence, voicemail, conferencing, and collaboration tools integration.
* Softphone and mobile client support.


6.2.6 Remote VPN / Work-from-Home
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Dual VPN concentrators in HA cluster with session replication.
* IPsec/SSL VPN with Dead Peer Detection (DPD).
* Zero-Trust policies with MFA, posture assessment, dynamic ACLs.
* Split/full tunnel modes as approved by the Authority.


6.3 Network Services (Common Across Domains)
--------------------------------------------

* **Routing:** OSPF / BGP with GR, NSF, and BFD (200–500 ms).
* **IP Services:** Redundant DNS/DHCP servers with synchronized IPAM.
* **AAA/NAC:** Centralized RADIUS / TACACS+ with redundant nodes.
* **Management:** Web GUI/SSH/SNMP using secure protocols (SSH v2, HTTPS, SNMP v3).


6.4 Addressing, Segmentation and Traffic Engineering
----------------------------------------------------

* Structured IPv4/IPv6 scheme: /16 region, /20 site, /24 segment.
* VRFs per domain (Corp, Guest, IoT, Voice, Mgmt).
* L3 Gateway HA via HSRP/VRRP (Campus) and Anycast Gateway (DC).
* ECMP for symmetric routing and optimal load sharing.


6.5 Security and Compliance
---------------------------

* Defense-in-depth architecture with segmentation, NAC, firewalls, IDS/IPS, SIEM.
* Administrative access via MFA and RBAC.
* Log retention ≥ 12 months; forward to central SIEM.
* Compliance with CIS Controls, ISO 27001, and NIST CSF.


6.6 Monitoring, Telemetry and Automation
----------------------------------------

* Real-time telemetry (SNMP v3, gNMI/gRPC, IPFIX/NetFlow).
* Site availability ≥ 99.95 %; routing convergence ≤ 500 ms (BFD).
* IaC automation with validation and rollback.
* Monthly SLA and capacity reports (ports, APs, VPNs, UC metrics).


7. Bill of Materials (BOM) and Licensing
=========================================

The Bidder **shall supply** all required active and passive components,
including switches, routers, controllers, APs, firewalls, servers, optics, cables,
and associated software licenses.

* All equipment **shall be new and of current production**.
* Licenses **shall include** five-year software and support entitlements.
* Quantities **shall** be confirmed during detailed design.


8. Implementation Plan and Timeline
===================================

* **Phase 1:** Detailed Design – 4 weeks
* **Phase 2:** Procurement & Staging – 6 weeks
* **Phase 3:** Deployment – 8 weeks
* **Phase 4:** Testing & Acceptance – 2 weeks
* **Phase 5:** Handover & Training – 2 weeks

Total implementation timeline ≈ 22 weeks (subject to site access).


9. Testing and Acceptance
==========================

* Factory Acceptance Test (FAT) and Site Acceptance Test (SAT)
  **shall** verify functionality, performance, and redundancy.
* Acceptance criteria include latency, throughput, failover time, and security policy validation.
* Comprehensive test reports **shall** be submitted to the Authority for approval.


10. Operations and Maintenance
==============================

* 24×7 technical support with defined SLA response times.
* Proactive monitoring via NMS and automated alerts.
* Firmware maintenance and patch management under vendor guidelines.
* On-site spare strategy for critical components.


11. Training and Documentation
==============================

* The Contractor **shall provide** comprehensive training for administrators and operations staff.
* Deliverables include System Design Document (SDD), As-Built Drawings, and Configuration Backups.
* All documentation **shall be provided** in editable electronic format and hard copy.


12. Service Level and Warranty Commitments
==========================================

* Minimum availability commitment: 99.95 % per site.
* Hardware warranty: 5 years comprehensive replacement.
* Software support: 5 years updates and security patches.
* Mean Time to Restore (MTTR): ≤ 4 hours for critical failures.
* Periodic SLA reviews and reporting to the Authority.

----

**End of Document**
