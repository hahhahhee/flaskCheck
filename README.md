# Flask Todo List Project (실습)

이 프로젝트(실습)는 **Flask** 웹 프레임워크와 **MongoDB** 데이터베이스를 사용하여 간단한 Todo List 애플리케이션을 구현한 예제입니다. 
사용자는 할 일 목록을 추가하고, 완료 상태를 변경하며, 항목을 삭제하거나 수정할 수 있습니다.

## 기능

- **Todo 항목 추가**: 사용자가 내용을 입력하여 Todo 항목을 추가할 수 있습니다.
- **Todo 항목 조회**:
  - **All list**: 모든 Todo 항목을 조회합니다.
  - **Active list**: 완료되지 않은 Todo 항목만 조회합니다.
  - **Completed list**: 완료된 Todo 항목만 조회합니다.
- **Todo 항목 수정**: 각 Todo 항목을 클릭하여 내용을 수정할 수 있습니다.
- **Todo 항목 완료 표시**: Todo 항목을 완료(또는 완료 취소)할 수 있습니다.
- **Todo 항목 삭제**: Todo 항목을 삭제할 수 있습니다.

## 기술 스택

- **Flask**: Python 기반의 웹 프레임워크
- **MongoDB**: NoSQL 데이터베이스
- **WTForms**: 웹 폼 처리를 위한 라이브러리
- **Jinja2**: Flask에서 HTML 템플릿을 렌더링하는 데 사용

## 설치 방법

1. **Python 설치**: 이 프로젝트는 Python 3.x 버전에서 실행됩니다. Python이 설치되어 있는지 확인하십시오.

2. **필요한 라이브러리 설치**:
   프로젝트의 의존성은 `requirements.txt`에 나열되어 있습니다. 아래 명령어로 필요한 라이브러리를 설치할 수 있습니다.

   ```bash
   pip install -r requirements.txt

## 시연 영상1 (메모 입력하기)
<video src="https://github.com/user-attachments/assets/e6562829-1785-456b-accc-156fd6b521b1" width="700" height="370" autoplay muted>

## 시연 영상2 (메모 수정 및 삭제하기)
<video src="https://github.com/user-attachments/assets/08188fa2-c841-4c43-8539-e027d008f61b" width="700" height="370" autoplay muted>
