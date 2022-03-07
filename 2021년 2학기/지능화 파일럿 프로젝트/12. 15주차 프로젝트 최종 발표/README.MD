# ** 프로젝트 최종 발표 ** 

- 프로젝트 최종 발표 
   + 반도체의 Bump Ball의 불량을 명확히 구분하기 위해 CNN의 일종인 ResNet-18로 진/가성 불량을 시도함
   + 기존의 전통적인 머신비전 검사 알고리즘에서 검사 Parameter를 Tight하게 관리하여 진/가성 불량이 혼재되도록 (미검출이 없도록) Setup
   + 기존의 알고리즘에서 불량으로 판정한 Bump Ball을 ResNet으로 진/가성 분류를 시도
   + Gray Image vs Real Color(RGB) vs Pseudo Color(불량의 특징이 명확한 Gray 영상들에 Color RGB를 각각 부여하여 하나의 Color 영상으로 병합)의 분류 정확성 비교 평가
   + Pseudo Color를 분류에 사용하는 경우가 다른 방식 대비 평균적으로 최소 1.2% 이상의 정확성을 보임
   + 합성곱 신경망 분류기의 성능을 높이기 위해 분류기 자체의 성능을 높일 수도 있지만 입력되는 영상을 전처리를 통하여 영상에 분류하고자 하는 특징을 더 많이 포함하는 것도 유용함을 확인함


[프로젝트 목표]</p>
<img src="./프로젝트 목표.jpg"  width="640" height="480"> 

[연구의 의의 및 고찰]</p>
<img src="./연구의 의의 및 고찰.jpg"  width="640" height="480"> 

[결론 및 요약]</p>
<img src="./결론 및 요약.jpg"  width="640" height="480"> 

<p align="center">
 
</p>
</br>
