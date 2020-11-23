# WSN


## Notes

```
ToA TDoA
CH7.2

Red 標註

Interactive multi

MCL
APIT

Sender / recevier sync
NTP
HRTC

## Routing
AODV***
Gossiping
BIP-example**
GPSR ***
GeRaF - example **

## MAC protocol
ALOHA
前段名詞
CSMA/CA RTS/CTS hidden terminal problem …. 

RFD FFD
15.4 MAC
RTS/CTS**
15.4 transfer mode 競爭與非競爭
省電 inaction portion

B-MAC(Zigbee
LEACH*
```


### CH7 Localizatino & Positioning
- ToA
    - Use : time of transmission
    - Propagatoin speed
    - Problem : Exact time synchronization
    - Propagatino speed depends on temp or humidity
- TDoA
    - Use two different signals with different propagation speeds
    - Problem: expensive/energy-intensive hardware
    - TDOA需要基站之間進行時間同步

```
TDOA需要基站之間進行時間同步

TDOA是用多個基站接收到信號的時間差來確定移動台位置，

TDOA值的獲取一般有2種形式： 第1種形式是利用移動台到達2個基站的時間TOA，取其差值來獲得，這時仍需要基站時間的嚴格同步，但是當兩基站間移動信道傳輸特性相似時，可減少由多徑效應帶來的誤差
```
- Iterative multilateration
    ```
	Assume some nodes can hear at least three anchors (to perform triangulation), but not all
	Idea: 
	let more and more nodes compute position estimates,
	spread position knowledge in the network
	Problem: 
	Errors accumulate
	When not all nodes in the network will have three nodes with position estimates
	
	假設一些nodes至少可以與3個anchors通訊
	方法:
	越來越多的nodes計算位置，一直往外延伸至整個網路
	問題:
	如果發生錯誤，則會一直累加
	可能會發生節點附近沒有3個以上的節點計算位置
	```
    - Solutions
    	```
    	方法1:增加參考節點
    	至少要有3個anchors或者附近有其他的參考節點
    	方法2:Sound
    	至少要有3個anchors的獨立參考點
    	Anchors的路徑不能有交集
    	方法2較適合數量少的anchor
    	```
        
- APIT : Approximate point in triangle
```
使用單純的連通性資訊
想法:使用任意三個anchor圍成三角形來決定所要定位的節點在內部還是外部
無論如何,移動的一個發送節點比較沒辦法有效率的去定出他的位置
解決方法: 確認所有鄰近節點彼此的位置後,大約在角落的地方給定三個anchor節點
```
- MCL : Monte-Carlo Localization
```
1. 時間分為很多個time slot.
2. 每個time slot會重複算一次自己的位置. 
3. 每個time slot, node移動距離是介於 [0, Vmax] 的區間內. 
4. 每個Anchor node定期廣播自己的location位置給2-hop鄰居.

在MCL中, 每個normal node 在每個time slot中　維持 50個samples, 
1. 每一個sample是一個座標位置, 代表這個normal node可能的位置. 
2. 由於normal node是持續的移動, 所以這個time slot的sample會與上一個time slot的sample 有一定的距離關係, 因此sample選擇的位置, 與上一個time slot的sample有關. 
3. 這些sample位置必須滿足三個條件, 必須要落在anchor constraint中

```


### Routing
- **AODV : Ad-hoc On demand Distance Vector**
    ```
    Very popular routing protocol
    Essentially same basic idea as DSR for discovery procedure
    Nodes maintain routing tables instead of source routing
    Sequence numbers added to handle stale caches
    Nodes remember from where a packet came and populate routing tables with that information 
    ```
    - Path Discover
        ```
        The Path Discovery process is initiated whenever a source node needs to communicate with another node for which it has no routing information in its table. 
        Every node maintains two separate counters: a node sequence number and a broadcast id.
        The source node initiates path discovery by broadcasting a route request (RREQ) packet to its neighbors.
        The RREQ contains the following fields:< source addr; source sequence #; broadcast id; dest addr; dest sequence #; hop cnt >
        ```
- BIP : Broadcast Incremental Power (CH. Routing p.45)
    ```
    How to broadcast, using the wireless multicast advantage?
    Goal: use as little transmission power as possible
    Idea: Use a minimum-spanning-tree-type construction (Prim’s algorithm)
    But: Once a node transmits at a given power level & reaches some neighbors, it becomes cheaper to reach additional neighbors 

    From BIP to multicast incremental power (MIP): 
    Start with broadcast tree construction, then prune unnecessary edges out of the tree 
    ```
- GPSR : Geometric Perimeter State Routing
    ```
    Geometric Perimeter State Routing (GPSR)
    Use greedy, “most forward” routing as long as possible
    If no progress possible: Switch to “face” routing
    Face: largest possible region of the plane that is not cut by any edge of the graph; can be exterior or interior
    Send packet around the face using right-hand rule
    Use position where face was entered and destination position to determine when face can be left again, switch back to greedy routing
    Requires: planar graph! (topology control can ensure that)

    ```
- GeRaF
    ```
    How to combine position knowledge with nodes turning on/off?
    Goal: Transmit message over multiple hops to destination node; deal with topology constantly changing because of on/off node 
    Idea: Receiver-initiated forwarding
    Forwarding node S simply broadcasts a packet, without specifying next hop node
    Some node T will pick it up (ideally, closest to the source) and forward it
    Problem: How to deal with multiple forwarders? 
    Position-informed randomization: The closer to the destination a forwarding node is, the shorter does it hesitate to forward packet
    Use several annuli to make problem easier, group nodes according to distance (collisions can still occur)
    ```
    
### CH3 MAC
- Reservation Based
    - TDMA : Time Division
    - FDMA : Frequency Division
    - CDMA : Code Division
- Contention Based
    - ALOHA
        - Pure ALOHA
            ```
            當想要傳送Data時，就直接往外傳送。
	        特點：在低traffic load 時成功率高，反之碰撞率高
            ```
        - Slotted ALOHA
            ```
            把頻道在時間上分段(slot)，每個傳輸點只能在一個分段(slot)的開始處進行傳送。每次傳送的數據必須少於或者等於一個頻道的一個時間分段(slot)。這樣大大的減少了傳輸頻道的衝突。
	        特點：改善了隨時隨地都有可能封包的缺點。

            ```
    - CSMA
    - MACA
        - RTS/CTS
            ```
            MACA的特色是要傳之前不用再去聽網路有沒有人在傳送。
            他用收到的RTS與CTS狀況來決定是幾是否可以傳送。
            收到RTS的區域是可以傳送的，因為碰撞是發生在收端，但收到RTS的人是沒辦法接收檔案的。
            收到CTS的區域代表是不能傳送資料給其他節點的。因為收到CTS代表他在Receiver的傳輸半徑內，如果此時送資料將會打斷Receiver的資料傳送。
            收到RTS與CTS的代表他不能接收資料也不能傳送資料。

            缺點：無線網路的傳送，相對於有線網路更容易發生封包遺失或者封包錯誤的事件出現。因為MACA把ACK機制拿去，使得沒辦法確認封包是否平安送達。
            這點在於無線網路是一個很嚴重的缺點。
            ```
- Hybrid
    - DAMA

- B-MAC (CH3 MAC p.89)
    ```
    B-MAC Goals：
    Low Power operation
    Effective collision avoidance
    Simple and predictable
    Small code size and RAM usage
    Scalable to large numbers of nodes

    B-MAC employs an adaptive preamble sampling scheme to reduce duty cycle and minimize idle listening
    
    B-MAC專注於處理link protocol問題，
    並不像是S-MAC之類的演算法有處理organization, synchronization,和routing built的問題
    B-MAC is a link protocol ,its services include, but are not limited to, target tracking, localization, triggered event reporting, and multi-hop routing

    B-MAC的目標是在節點間建立一個低耗能且可靠的傳輸方法

    為了達成可靠的傳輸，B-MAC使用了Clear Channel Assessment (CCA)避免collision的發生，CCA演算法可以判斷channel是否適合傳輸資料

    為了讓達成低耗能的目標，B-MAC使用了low power listening (LPL)演算法讓sender能夠在需要傳輸資料時，能確實通知receiver
    ```
- LEACH
    ```
    LEACH特別適用於廣大範圍蒐集資料的場景中，例如要蒐集大量的資料回sink的監測工作
    在LEACH的階層式架構中，不但可以平均電量的消耗，同時能夠讓傳輸至sink的資料聚集後再傳輸

    在LEACH中，使用了clustering-based的階層式網路架構，cluster head可以集中管理每個node的通訊，
    並且將要送到sink的資料聚集壓縮後在傳輸，已達到最佳化傳輸的效果

    在每個cluster head中，可以使用CDMA code減少傳輸時的collision問題，讓cluster中的傳輸效率提昇

    為了考慮到平均電量消耗，LEACH會定時改變cluster的架構，
    一定時間過後，電力使用較少的節點會成為新的cluster head，藉此平均網路中的電量消耗

    ```
    
### CH6 Time Synchronization
- NTP : Network Time Protocol (CH6 p.11)
- HRTS : Hierarchy Reference Time Synchronization (CH6 p.69)
    ```
    Goal :
    synchronize the vast majority of a WSN in a lightweight manner

    Idea 
    combine the benefits of LTS and RBS 
    ```
