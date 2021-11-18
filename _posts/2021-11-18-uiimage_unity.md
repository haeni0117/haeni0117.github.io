---
title: "[unity] UI image, texture ..."
categories:
  - unity
tags:
  - UI
  - image
  - texture
  - unity
last_modified_at: 2021-11-18T09:06:00-05:00
---
## 텍스쳐(Texture) 
- 텍스쳐(texture) : 유니티 엔진에서 사용되는 이미지 리소스
- 스프라이트(Sprite) : 이 텍스쳐 중에서도 <u>Image 컴포넌트나 2D 게임의 오브젝트로 그려지는 스프라이트 렌더러에서 사용되는 리소스들
  
텍스쳐(Texture) ⊂ 스프라이트(Sprite)

- 자동으로 Texture Type이 Default로 정해진다 → Default는 주로 3D 모델 오브젝트의 텍스쳐로 사용되는 타입
- UI에 사용하기 위해서는 이 Texture Type을 Sprite로 변경해야함
  - 임포트한 텍스쳐들을 선택하고 Texture Type을 Sprite로 변경
  
  
  
## Image 컴포넌트
- 유니티 엔진에서 화면에 그림을 표현하기 위해 사용
- 프로퍼티(property) : Source Image, Color, Material, Raycast Target
  
  
  
