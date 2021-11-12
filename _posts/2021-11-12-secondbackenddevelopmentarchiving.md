---
title: "백엔드 개발자를 꿈꾸는 학생개발자에게 - 2 "
categories:
  - Back-end
tags:
  - Back-end
  - Archiving
last_modified_at: 2021-11-12T08:06:00-05:00
---
# 백엔드 개발에 필요한 지식
## Q 백엔드 개발을 하려면 어떤 지식이 중요하고 무엇을 기본적으로 알아야 할까요? 백엔드 개발 전문가는 어떤 언어, 툴, 주제를 공부하고 개발하나요? 프로젝트 스킬셋을 결정하는데 고려되는 부분들은 어떤 것들이 있나요?
- 주로 JVM과 Linux를 바탕으로 한 환경에서 서버 모듈 개발했다.
---
- 웹 생태계의 스펙
  - HTML, HTTP(1.1 , HTTP/2)
- 기본 SDK, 라이브러리/프레임워크 이해와 활용
- 클라이언트를 위한 API 설계
- 서버/컴퍼넌트/객체 간의 역할 분담/의존성/통신 방법 설계
- 저장소 활용
  - DBMS 설계
  - Cache 적용
    - Global/Local cache 적용범위, 라이프 싸이클, 솔루션 선택
  - 파일 저장 정책/솔루션 선택 활용
- 검색엔진 연동 방식 결정
- 빌드 도구
  - Maven/Gradle
- 배포 전략
- 성능 테스트/프로파일링/튜닝
  - JVM 레벨의 튜닝 (GC 옵션 등)
    - 웹 서버(Nginx,Tomcat)등의 설정/튜닝
  - OS 설정의 주요 값 확인
- 인접 기술에 대한 이해
  - DBMS, Front End 등
- 서버 개발자에만 해당하지는 않는 항목
  - 테스트 코드 작성/리팩토링 기법
  - 버전 관리 전략
    - branch 정책 등
    
---
- 개발자 한 명이 위에 언급한 모든 요소를 깊이 잘 알아야 프로젝트에 참여할 수 있어야한다는 의미는 아니다.
- 팀을 이룬 개발자들의 지식들이 합쳐져서 구현 방식과 정책이 결정된다.
  - 사용자가 많은 서비스(위험성 높음) : 프로그램이 돌아가는 만드는 것만이 목적이 아니기 때문에 기술의 선택에 더 조심스러워진다. 운영환경에서의 모니터링과 문제해결까지 팀 구성원이 할 수 있는 기술을 선택한
  - 내부의 소수만 사용하는 관리 도구(위험성 낮음) : 상대적으로 부담 없이 팀원 모두가 처음 쓰는 기술을 적용하기도 한다. 새로운 기술은 위험성이 적은 서비스에 적용해서 경험을 키운 이후에 큰 서비스에 적용을 한다.

# 데이터베이스
## Q 데이터베이스를 어디까지 알아야하나요?? 데이터베이스를 어떻게 활용하는 것이 효율적인가요? 쿼리를 어떻게 만들고 튜닝해야할까요?
- 사용자의 요청량과 저장 용량이 많은 서비스에서는 하나의 저장소만을 쓰지는 않는다.
  - 네이버의 서비스 : MySQL, CUBRID, Redis, Memchaced, HBase, MonoDB, Elasticsearch 등 다양한 저장소를 활용하고 있다.
  - 네이버와 라인 : Arcus, Elasticsearch, Cassandra, Redis, HBase와 같은 다양한 저장소가 쓰인 사례가 있다.
- 다양한 저장소가 쓰이는 시대에도 RDB(관계형 데이터베이스)는 여전히 가장 우선시되는 저장소이다. 
  -  RDB를 잘 다루는 능력은 백엔드 개발자의 핵심 역량 중 하나이다.
  -  개발을 하는 도중에도 쿼리의 호출 횟수나 실행 계획이 비효율적이지 않은지 확인하는 습관이 필요하다.
  -  운영 중에도 느린 쿼리를 모니터링하고 DBA와 협업하여 성능 개선을 하는 작업을 실무개발자들은 꾸준히 하고 있다.
  -  ORM같은 추상화된 프레임워크를 써서 직접 SQL을 작성하지 않는 경우에도 그런 작업들은 더욱 중요하다.
- 대용량 서비스들을 보면 DB 쿼리를 만드는 스타일이 과거와는 달라졌다.
  - 과거 : 서버 간의 네트워크 호출 비용을 줄이기 위해 굉장히 많은 테이블을 한번에 조인하는 긴 SQL을 만드는 경우가 많았다. 
  - 요즘 : 복잡한 JOIN은 가급적 피하는 경향이 생겼다. -> 데이터를 조회하는 SQL이 단순할수록 데이터를 다른 저장소에 캐시하거나 분산해서 저장하기가 쉬워진다.
  - 대용량을 저장하는 UGC 서비스 : RDB 테이블 사이의 JOIN은 최대한 제약을 하고, 어플리케이션 레벨에서 여러 저장소의 연관된 데이터를 조합하기도 한다.
Stored prodecure도 가급적 사용하지 않는 경우가 많