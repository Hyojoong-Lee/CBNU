# ** 프로젝트 9주차 진행 사항 보고 ** 

- ResNet-18을 이용한 분류 성능 Test 진행
    + 먼저 Real Color 영상과 R(경사조명), G(동축조명), B(동축광량30%) 로 구성한 Pseudp Color 영상의 인식률 비교
    + Real Color의 Best Acc = 82.4%. Pseudo Color의 Best Acc = 84.9%로 약 2.5%의 개선효과를 확인
    + 예상보다 개선율이 낮아 (82.4% >> 84.9%), Pseudo Color 조합 방식을 변경함
    + Blue 채널에 사용되는 영상에서 불량의 특성이 명확히 드러나지 않아 해당 채널 삭제 및 구성 변경
    + 기존 Blue 채널 삭제로 빈 컬러 채널에 특징이 명확한 기존의 영상을 추가하여 성능 개선을 시도
    + 이때 빈 영상을 추가할 경우 성능 저하가 우려되어 기존 영상을 추가  
[Pseudo Color 조합 방식 변경]</p>
<img src="./영상 조합 방식 변경.jpg"  width="640" height="240"> 

- Pseudo Type2를 ResNet-18로 분류 진행. 
    + Real Color의 Best Acc = 82.4%. Pseudo Color의 Best Acc = 84.9%, Pseudo2 Color의 Best Acc = 87.2%
    + 반복성 확인을 위해 Pseudo2를 1회 추가 Test한 결과 Acc는 86.2%

[1차 Real Color VS Psedo Color 결과]</p>
<img src="./ResNet_18 1Test.jpg"  width="640" height="340"> 

[2차 Real Color VS Psedo Color VS Pseudo Color Type2 결과]</p>
<img src="./ResNet_18 2차 Test.jpg"  width="640" height="340"> 

<p align="center">
 
</p>
</br>