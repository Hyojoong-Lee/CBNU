# **산업컴퓨터비전실제 Final Term Proj.** 

- 기말고사 대체. Mid Term Report를 기반으로 현업에서 필요로 하는 Issue에 대한 문제 제기와 해결 방안
- Issue
  + 대면적 Package의 Stitching 알고리즘 개선
     * Open CV의 Stitching 알고리즘으로 Vision System의 FOV보다 큰 Package의 영상을 분할 획득하여 각 조명 조건 별 Stitching을 시도.
     * 특징점이 명확할 경우 별도의 설정 없이 Stitching이 가능하나, 특징점이 부족할 경우 실패.
     * 이와는 별개로 본사에 개발 중인 Vision System에 해당 기능 적용 Test 예정 -> 2021/03월 Test 결과 특징점이 없는 영역이 많아 실패. 
  + 위와는 별개로 Wafer의 Crack을 검사하기 적합한 영상을 추출하기 위해 필요한 기능에 대해 정리
     * Wafer에 연마흔이 남아 있는 경우 Crack과 연마흔의 구분이 어려움
     * 조명을 60deg 간격으로 3장의 영상을 획득하여 검사에 적합한 영상을 찾는 기능 필요
        

- Final-Term Project_이효중_stitching.pptx : 프로젝트 개요
- FianlTermProj.py : OpenCV의 Stitcher 함수로 구현한 대면적 Package의 Stitch Code

<p align="center">
  
</p>
</br>