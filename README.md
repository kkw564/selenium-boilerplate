## 0. 셀레니움 실행을 위한 chrome 드라이버 다운로드

사용중인 chrome 버전으로 드라이버를 다운로드 한다.

크롬 버전 확인 (주소창에 복붙)

chrome://version

크롬 드라이버 다운로드 링크

chromedriver.chromium.org/downloads

## 1. 셀레니움 설치 및 import, 기본 코드

1. selenium 설치 pip코드

   pip install seleum

2. import 및 기본 코드

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("크롤링 할 주소 입력")
driver.implicitly_wait(3)
```

## 2. 브라우저 탭 이동/ 앞으로, 뒤로 / 닫기

```python
탭 이동
driver.window_handles[0] #브라우저 탭 객체를 리스트로 반환. [0] 은 첫번재 탭을 의미
driver.switch_to.window(driver.window_handles[0]) #첫번째 탭으로 이동
driver.switch_to.window(driver.window_handles[1]) #두번째 탭으로 이동
driver.switch_to.window(driver.window_handles[2]) #세번째 탭으로 이동

뒤로가기 / 앞으로가기
driver.back() #뒤로가기
driver.forward() #앞으로가기

탭닫기 / 브라우저 닫기
driver.close() #현재 탭 닫기
driver.quit() #브라우저 닫기
```

## 3. (xpath / class_name / id / css_selector ...)

원하는 부분의 xpath 등을 가져와서 클릭하여 페이지 이동과 같은

행동을 할 수 있다.

```python
driver.find_element_by_xpath('//\*[@id="main-area"]/div[7]/a[2]') #xpath 로 접근
driver.find_element_by_class_name('ico_search_submit') #class 속성으로 접근
driver.find_element_by_id('k_btn') #id 속성으로 접근
driver.find_element_by_link_text('회원가입') #링크가 달려 있는 텍스트로 접근
driver.find_element_by_css_selector('#account > div > a') #css 셀렉터로 접근
driver.find_element_by_name('join') #name 속성으로 접근
driver.find_element_by_partial_link_text('가입') #링크가 달려 있는 엘레먼트에 텍스트 일부만 적어서 해당 엘레먼트에 접근
driver.find_element_by_tag_name('input') #태그 이름으로 접근

이중으로 find_element 를 사용 할 수 있다.
#input 태그 하위태그인 a 태그에 접근
driver.find_element_by_tag_name('input').find_element_by_tag_name('a')

    #xpath 로 접근한 엘레먼트의 안에 join 이라는 속성을 가진 tag 엘레먼트에 접근

driver.find_element_by_xpath('/html/body/div[3]/form//span[2]').find_element_by_name('join')
```

## 4. 클릭 .click()

```python
driver.find_element_by_xpath('//\*[@id="main-area"]/div[7]/a[2]').click()
```

## 5. 텍스트 입력/엔터 .send_keys('텍스트') / .send_keys(Keys.ENTER)

```python
driver.find_element_by_name('query').send_keys('보라매역')
driver.find_element_by_name("query").send_keys(Keys.ENTER)
```

## 6. 텍스트 삭제 .clear()

```python
driver.find_element_by_name("query").clear()
```

## 7. iframe 지정 switch_to.frame

```python
#iframe 지정
element = driver.find_element_by_tag_name('iframe')

#프레임 이동
driver.switch_to.frame(element)

#프레임에서 빠져나오기
driver.switch_to.default_content()
```

## 8. 팝업창 이동 / 수락 / 거절

```python
#경고창으로 이동
driver.switch_to.alert

from selenium.webdriver.common.alert import Alert

Alert(driver).accept() #경고창 수락 누름
Alert(driver).dismiss() #경고창 거절 누름
print(Alert(driver).text # 경고창 텍스트 얻음
```

## 9. 스크롤 내리기

```python
#브라우저 스크롤 최하단으로 이동
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
```

## 10. 스크린샷

```python
#캡쳐할 엘레먼트 지정
element = driver.driver.find_element_by_class_name('ico.target')

#캡쳐 (name에는 파일명)
element.save_screenshot('name.jpg')
```

## 11. 오류 예외 처리 try , except문

클릭이나 프레임 이동시 에러가 발생 할 경우 사용할 수 있다

```python
try:
print('') #실행할 코드

except:
pass #오류 발생시 실행할 코드
pass를 사용하면 오류를 회피한다.

#예시
try:
name = driver.find_element_by_tag_name('table')

    except NoSuchElementException:   #except 오류문(해당 오류가 발생시 실행)
        print(" [예외 발생] 표 없음 ")
        continue

    except 오류문2:  #오류문 여러개 사용가능

    else:	#오류가 없을시 try문 다음으로 실행한다.
    	print('오류가 없어요')
```

## 12. 여러가지 오류문 모음

여러가지 오류 모음

```python
# NoAlertPresentException 경고창 관련 명령어를 실행했으나 현재 경고창이 뜨지 않음

# NoSuchElementException 엘레먼트 접근하였으나 없음

# TimeoutException 특정한 액션을 실행하였으나 시간이 오래 지나도록 소식이 없음

# ElementNotInteractableException 엘리먼트에 클릭등을 하였으나 클릭할 성질의 엘리먼트가 아님

# NoSuchWindowException 해당 윈도우 없음

# NoSuchFrameException 해당 프레임 없음
```
