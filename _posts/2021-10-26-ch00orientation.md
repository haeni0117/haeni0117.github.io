#  배틀 로얄 제작을 위한 알고리즘과 프레임 워크 - 오리엔테이션
- 8년 전에는 유니티로는 작은 수준의 모바일 게임밖에 만들지 못했음
- 클라이언트 용량 한계 있었음 
- rpg project 
  - RPG란?
    - 롤플레잉 게임(영어: role-playing game, RPG)은 참가자는 각자에게 할당된 캐릭터 (플레이어 캐릭터)를 조작하고 일반적으로는 서로 협력하여 가상의 상황에서 주어지는 시련을 극복하고 목표 달성을 목표로 하는 게임의 일종이다.
    - RPG게임의 예시 : 타임리버스
    - ![image](https://user-images.githubusercontent.com/69496570/138952308-bb95ae4d-7073-4707-9db2-cd33919be86d.png)
    - 배틀그라운드(battle ground) : 3인칭 슈팅게임 
    - RPG + 전략시뮬레이션 ... etc
- 배틀그라운드 프레임워크
- 배틀그라운드 게임 인공지능 및 최적화
- 강의대상 : 취준생 + 색다른 포트폴리오 제각에 관심있는 사람 , 유니티 엔진개발기법(실무), 중급이상, 3인칭 슈팅게임
- 강의방식
  1. 필수 이론 설명
  2. 작업의 목적 설명
  3. 하나씩 직접 코드로 개발

# project 살펴보기 - 01. 게임 리소스 내려받기 (ch4 배틀그라운드 게임 제작을 위한 알고리즘/프레임워크)
- 아무리 중급이라도 현업개발자 기준이 아니기 떄문에, 천천히 ok!
- 22시간 내에 게임만들기
- 깃헙주소 : [https://github.com/seyoungChu/fc02_lecture](https://github.com/seyoungChu/fc02_lecture)
- Git GUI 소스트리(SourceTree) : 개발자들끼리 리소스(resource)를 주고받는 형상관리
  - 형상관리란? 형상관리란? 위키피디아 : 소프트웨어의 변경사항을 체계적으로 추적하고 통제하는 것으로, 형상 관리는 일반적인 단순 버전 관리 기반의 소프트웨어 운용을 좀 더 포괄적인 학술 분야의 형태로 넓히는 근간을 이야기한다. 형상관리는 변경사항을 체계적으로 추적, 통제한다는 것.
    - 즉, 개발과정 버전관리 -> 근데 이건 github으로 하면 되지 않나...? 그냥 깃헙처럼 버전관리하는 서비스라고 생각하면 될 듯!
    - 깃허브데스크탑(githubdesktop)과 소스트리(sourcetree)의 차이점 : [https://hyuntaekhong.github.io/blog/GIT-GUI-TOOL/](https://hyuntaekhong.github.io/blog/GIT-GUI-TOOL/)
     - 형상관리란? 형상관리란? 위키피디아 : 소프트웨어의 변경사항을 체계적으로 추적하고 통제하는 것으로, 형상 관리는 일반적인 단순 버전 관리 기반의 소프트웨어 운용을 좀 더 포괄적인 학술 분야의 형태로 넓히는 근간을 이야기한다. 
     - 차이점 : 사용자 인증을 주기적으로 해야한다는 점이 단점으로 많이 언급되고 있습니다. 그러나 Github Desktop보다 고도화된 기능과 작업을 지원하는 엔터프라이즈급 툴이라는 것이 강점
      - github 데스크탑 단순한 건 인정, 근데 난 맨날 1인개발만 하니까 데스크탑 계속 쓸 것이다. -> 대형플젝아니라는 소리... 쪼렙개발자라는 소리....
  - 출처 : [https://smoothroutine.tistory.com/104](https://smoothroutine.tistory.com/104)
- 버전관리하는 대표적인 서비스 : git, SDN
  - [SDN이란?](https://www.juniper.net/kr/ko/research-topics/what-is-sdn.html)
  - SDN(Software-Defined Networking)은 <mark>네트워크 리소스를 최적화하고 변화하는 비즈니스 요구 사항, 애플리케이션, 트래픽에 맞춰 네트워크를 신속히 적응시키기 위한 네트워크 가상화 및 컨테이너화 접근 방식<mark>입니다. SDN은 네트워크 컨트롤 플레인과 데이터 플레인을 분리하여 물리적 장비와 구분되는 소프트웨어 프로그래밍이 가능한 인프라를 생성함으로써 구현됩니다.
    - 네트워크 컨트롤 플레인
    - 데이터 플레인(Data Plane) : 서비스 간 네트워크 트래픽을 관리하는 서비스 메쉬 애플리케이션 -> 사이드카(정확히는 로컬 프록시들의 모음)가 곧 데이터플레인
      - 로컬 프록시(local proxy) : 로컬 프록시는 들어오는 TCP 연결의 수신자 또는 발신자 역할을 하는 프로세스입니다. 이 프록시는 WebSocket 보안 연결에서 보안 터널링 서비스를 통해 디바이스 애플리케이션에서 보낸 데이터를 전송합니다.
      - TCP : TCP (Transmission Control Protocol)는 IP 네트워크의 두 컴퓨터 간의 연결 지향 통신을 위한 전송 계층 호스트 간 프로토콜입니다. TCP는 가상 포트를 사용하여 두 컴퓨터 간의 물리적 연결을 재사용 할 수 있는 가상 종단 간 연결을 만듭니다.
    - 서비스메쉬(service Mesh) : 서비스 메쉬란 한 애플리케이션의 다양한 부분들이 통신하는 것을 제어하는 방법이다. 한 애플리케이션 안에서 여러 서비스들이 서로 통신하며 데이터를 주고받는 것을 서비스의 소스코드와 상관없이 제어하는 것이다. 
      - 서비스의 소스코드랑 상관없다는 점이 신기하다
      - service mesh랑 MSA는 엄연히 다르다. 
        - service mesh : how to control
        - MSA : structure of application
      - 서비스메쉬의 핵심은 추상화(abstraction)!!! 
        - -> 뭐든 추상화하는 게 좋긴 하겠지만, 서비스개수와 커뮤니케이션의 복잡도에 따라 효율성에 직격타를 맞을 수 있는 만큼 더 강조하나보다.
    - 출처 : [https://2kindsofcs.tistory.com/47](https://2kindsofcs.tistory.com/47)

  
  - 출처 : [https://smoothroutine.tistory.com/104](https://smoothroutine.tistory.com/104)
