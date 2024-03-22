# 목차

1. **서비스 소개**
2. **기획 배경**
3. **기능 소개**
4. **기술 스택**
5. **프로젝트 일정 및 산출물**
6. **개발 멤버 및 회고**

---

# Bank-juice 서비스 소개

## 서비스 설명

### 개요

- 한줄 소개 : 나에게 맞는 금융상품을 찾고 추천받는 서비스
- 서비스 명 : **Bank Juice**

### 타겟 🎯

- 한국어를 배우는 외국인들
- 자신의 발음이 올바른지 확인하고 싶은 외국인들
- 자신이 작성한 한국어 문장의 의미가 맞는지 확인하고 싶은 외국인들

# 🍌 기획 배경

## 목적 🥅

**한국어 작문 실력과 한국어 발음 실력을 늘려보자**

## 의의

- 외국인들이 한국인의 자문 없이도 효율적으로 한국어를 학습할 수 있다.
- 한국어를 쉽게 공부하면서 한국 문화에 수월하게 적응할 수 있다.
- 외국인뿐만 아니라 한국어가 서투른 한국인도 함께 공부할 수 있다.

# 🌽 기능 소개

## 시연 영상 💢

[Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/f1e47a0d-9501-4a61-a5ef-bdfc5dbac454/Untitled.mp4)

### 1. 홈페이지

- 로그인, 회원가입을 할 수 있는 시작 페이지 구현
- 발음 평가, 작문 평가 서비스로 넘어갈 수 있는 메인 페이지 구현
- Footer에 각 기능으로 넘어갈 수 있는 네비게이션 바 구현
- **화면**
    
    
    시작 화면
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/e20b9782-2cb4-48e0-974a-75825e2b5b33/Untitled.png)
    
    회원가입
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/2f929b39-a446-4297-9d18-a63f72f206ac/Untitled.png)
    
    로그인
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/1a072b45-a46d-4c0a-9f05-12ab02eb8cc1/Untitled.png)
    
    메인 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/367d602d-459b-4606-b8ef-2f68daf81e6f/Untitled.png)
    

### 2.  발음 평가 서비스

- 발음을 녹음할 수 있는 녹음기 서비스 구현
- 발음이 정상적으로 입력되었을 땐 점수를 평가해 보여주는 서비스 구현
- 발음이 정상적으로 입력되지 못했을 땐 Fail
- 마지막엔 최근 기록들을 보여주는 결과 페이지 구현
- **화면**
    
    
    녹음 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/78da2202-3757-4197-b8ed-546b0e45beec/Untitled.png)
    
    실패 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/83d9c798-f23a-494d-81a6-65f871042ffc/Untitled.png)
    
    성공 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/dc601e5b-a07a-4ebe-b1c5-2079ef8fd620/Untitled.png)
    
    결과 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/2166ee62-f450-4ed4-8ec3-995180c3f32e/Untitled.png)
    

### 3.  작문 평가 서비스

- 사용자가 번역해야 하는 영어 추천 문장 제공 (사용자가 직접 수정 가능)
- Papago API를 통해 영어 문장을 한국어 문장으로 번역(정답 문장)하여 데이터베이스에 저장
- 사용자가 한국어로 번역한 문장과 정답 문장 간의 유사도 평가
- 유사도 평가에 통과하지 못했을 경우 Fail
- 마지막엔 최근 기록들을 보여주는 결과 페이지 구현
- **화면**
    
    
    작문 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/d7d41d70-8993-447a-b853-1725ca550377/Untitled.png)
    
    성공 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/d5b5eabc-28c8-45c6-ae17-1986f650aedd/Untitled.png)
    
    실패 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/ae0bb5fd-bb99-462f-bcc5-1dc46c938235/Untitled.png)
    
    결과 페이지
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/7e316fd1-f4ae-4905-b56d-06fc6b7efe71/Untitled.png)
    

### 4. 마이페이지

- 사용자가 가지고 있는 경험치 표시
- 사용자의 경험치에 따라 티어 및 프로필 사진 자동 업데이트
- 발음/작문 평가 최근 기록 페이지 구현
- **화면**

# 🍩 기술 스택

### 1. DJango Simple JWT

💡**JWT 란?**

모바일이나 웹이 사용자 인증을 위해 사용하는 암호화된 토큰을 의미합니다. JWT는 인증에 필요한 모든 정보를 담고 있기 때문에 인증을 위한 별도의 저장소가 없어도 되며, 모바일에서 잘 동작하는 인증,인가 방식 입니다.

![Screenshot 2023-12-18 at 10.59.00 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/e71e79a9-fe70-44f3-b654-7cb4e85d7a61/Screenshot_2023-12-18_at_10.59.00_PM.png)

> **django simple JWT**
> 
> 
> DRF(Django REST Framework)를 위한 JWT 인증 플러그인입니다. 한 개의 토큰으로 모든 세션을 관리해야하는 Built-in Token 대신, access token과 refresh token 모두 간단하게 구현할 수 있는 django simple JWT를 사용하였습니다.
> 

**적용**

Korean Making은 모바일에서의 간단한 인증을 위해 Django Simple JWT를 사용합니다.

### 2. Azure AI Speech Service

> 음성 서비스는 [음성 리소스](https://learn.microsoft.com/ko-kr/azure/ai-services/multi-service-resource?pivots=azportal)를 통해 음성 텍스트 변환 및 텍스트 음성 변환 기능을 제공합니다. 높은 정확도로 음성을 텍스트로 변환하여 대화 내용을 기록하고, 자연스러운 텍스트 음성 변환을 생성하고, 음성 오디오를 번역하고, 대화 중에 화자 인식을 사용할 수 있습니다.
(출처 : https://learn.microsoft.com/ko-kr/azure/ai-services/speech-service/how-to-pronunciation-assessment?pivots=programming-language-python)
> 

![azspeech.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/72891cd4-b789-40b9-a1e0-663da05bc9b7/azspeech.png)

**적용**

Korean Making은 사용자가 읽은 한국어 문장 녹음 파일을 Azure AI Speech Service를 통해 발음평가 결과를 제공합니다.

### 3. ETRI 문장 패러프레이즈 인식 API

> 두 개의 문장이 동등한 의미를 가지는지 여부를 판별하는 기술로서, HTTP 기반의 REST API 인터페이스로 JSON 포맷 기반의 입력을 지원하는 Open API입니다.
> 

**적용**

Korean Making은 작문 평가 서비스에서 사용자가 입력한 한국어 문장과 정답 문장 간의 패러프레이징 결과를 제공합니다.

### 개발환경

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/435c17e5-3295-4d33-bd39-b3a57561e2ee/Untitled.png)

# 🍆 프로젝트 일정 및 산출물

## 프로젝트 진행

### Jira

---

- 매일 오후 회의에서 전날에 완료하지 못한 이슈나, 앞으로 진행할 이슈들을 추가함
- 에픽은 BE, FE 으로 구성
- 작업 현황을 실시간으로 Jira에 반영하여 현재 팀원이 어떤 작업을 하고있는지, 일정에 딜레이가 있는지 한 눈에 알아볼 수 있게 함

![Screenshot 2023-12-12 at 10.43.20 PM.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/383486b7-cea6-4401-bd4a-0a8c91afae0f/Screenshot_2023-12-12_at_10.43.20_PM.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/edb602ef-7f3c-4556-965d-1e6154762e9e/Untitled.png)

## 프로젝트 산출물

### 1. Figma

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/99e309f1-58e3-4ec7-9d93-d3b3d7d88df0/Untitled.png)

### 2. ERD

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d6911ec5-888c-412e-8308-fa7088b37868/9dd5b2c1-d6b3-4361-bbc9-4af88e895c2b/Untitled.png)

# 🍟 개발 멤버 및 회고

## 담당 역할

**공통**

- 프로젝트 설계
- ERD 설계
- Figma 목업

**오희주**

- **팀장**
- **Front-end**
- README 작성

**배정식**

- **Back-end**
    - 서버 기본 세팅
    - 서버 구현 보조 및 검토
- **Front-end**
    - 각 페이지 화면 구상
    - 페이지 스타일링
    - 로고 제작
- PPT 보조

**이윤정**

- **Back-end**
    - Writing API 구현
    - 유저 기본 기능 구현
- PPT 작성
- 영상 제작

**전세진**

- **Back-end**
    - Speaking API 구현
    - JWT 기반 인증 구현
- PPT작성

# 🤔 성과 및 배운 점

### 1. 외부 API 의존성 및 검증의 중요성

⚠️ **Problem**

프로젝트 초반 발음평가와 작문평가 모두 ETRI API를 이용했습니다. 그 과정 중 ETRI 전체 서버 점검으로 인해 주요 기능 모두 테스트에 어려움을 겪었습니다. 또한 발음평가 API의 경우 pcm파일만을 허용하고, 내부 오류로 인하여 발음평가 서비스 제공에 어려움이 발생했습니다.

**📝** **Learned**

프로젝트 종료 후, 좀 더 안정적인 서비스를 제공하기 위해 Azure speech AI Service로 API를 교체하였습니다. ETRI 주관 공모전이었기 때문에 사용한 API였지만, 이 경험을 바탕으로 API를 사용하기 전 충분한 검증의 중요성에 대해 배우게 되었습니다.

### 2. 소통과 문서화의 중요성

⚠️ **Problem**

2주일이라는 짧은 기간 동안 프로젝트를 진행하면서, 기획 과정에서 빠르게 정해진 세부 사항들이 제대로 공유되지 않아 계속해서 다시 확인해야 했던 어려움이 있었습니다. 

**📝** **Learned**

이에 프로젝트의 지속 가능성을 위해 코드와 시스템에 대한 충분한 문서화가 필요하다는 것을 배웠습니다. 또한 프론트에서는 백엔드에 데이터가 어떤 형식으로 보내져야 좋은지 적극적으로 어필하고, 백엔드에서는 프론트엔드로 전달되는 API 명세를 명확히 정의하고 문서화하는 것이 중요하다는 것을 배웠습니다. 이를 통해 각자 예상되는 데이터와 응답 형식을 명확히 이해할 수 있었습니다.
