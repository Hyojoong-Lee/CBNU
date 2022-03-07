# ** 프로젝트 13주차 진행 사항 보고 ** 

- ResNet-18을 이용한 분류 성능 Test 진행
    + ResNet의 특성 상 난수에 의한 계산과정이 존재하여 Pseudo Color Type 2와 Real Color 영상에 대해 각 5회 씩 반복 검증 진행.
    + 5회 반복 Test 결과 Real Color의 Max 값이 개선 영상의 Min과 유사하며, 평균 2.6%의 개선효과를 확인하였음
    + Pseudo Color를 생성하는데 사용한 Gray Image에 대한 정확성 Test 를 각 3회 씩 진행.
        * 경사 조명 영상 : 1차 85.9%, 2차 83.3%, 3차 85.3%
        * 동축 조명 영상 : 1차 76.6%, 2차 74.7%, 3차 72.8%
        * Real Color나 Gray 대비 Pseudo Color 방식의 정확률이 높음을 확인함

[반복 Test 결과]</p>
<img src="./반복 Test 결과 보고.jpg"  width="640" height="340"> 

<p align="center">
 
</p>
</br>