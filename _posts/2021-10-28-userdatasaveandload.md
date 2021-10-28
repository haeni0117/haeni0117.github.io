---
title: "사용자 데이터 저장/불러오기 - 1"
categories:
  - ComputerNetwork
tags:
  - userData
last_modified_at: 2021-10-28T08:06:00-05:00
---
플레이어 데이터를 저장하고 사용하는 과정
# firebase의 데이터베이스 보안법칙
- firebase란?
  - ![image](https://user-images.githubusercontent.com/69496570/139238381-2ac014df-432a-4ab3-8151-0e6a7f92152d.png)
# 보안규칙
보안규칙 : 읽기와 쓰기에 대한 권한 결정
- `.read` : 데이터를 읽을 수 있는 조건
- `.write` : 데이터를 쓸 수 있는 조건
```
"rules":{
  "all_scores" : {
    ".read" : "true", 
    ".write" : "true",
    },
  "users" : {
    "&uid" : {
      ".read" : "auth != null",
      ".write" : "auth != null && $uid === auth.uid",
    }}
}
```
- 위의 코드는 firebase에서 테스트해볼 수 있다.
- `$uid` : 유저아이디, 만약 id가 tim이라고 한다면 user 밑에 tim(user id)이라는 필드를 만들고 그 하위필드 밑에 데이터를 저장한다.
- `auth` : firebase에서 미리 설정된 변수 -> 인증된 사용자에 대한 정보(token, 토큰) 
  ```
   ".read" : "auth != null",
  ```
  - 사용자가 로그인을 했으면 데이터 접근 가능
  ```
  ".write" : "auth != null && $uid === auth.uid",
  ```
  - 사용자가 로그인완료 + 로그인한 사람의 아이디(uid) == auth.uid 까지 만족시켜야 데이터를 쓸 수 있다. -> 규칙지정
