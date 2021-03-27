from durable.lang import *

with ruleset('Solution'):
    #기본 정의
    @when_all((m.subject == 'Ball 검사') & (m.object == '검출력 이슈가') & (m.predicate == '발생 했다'))
    def categoryBallInsp(c):
        c.assert_fact({'subject': c.m.subject, 'object': '사전 정의 검사 항목', 'predicate': '이다'})

    @when_all((m.subject == 'Land 검사') & (m.object == '검출력 이슈가') & (m.predicate == '발생 했다'))
    def categoryLandInsp(c):
        c.assert_fact({'subject': c.m.subject, 'object': '사전 정의 검사 항목', 'predicate': '이다'})

    @when_all((m.subject == 'Crack 검사') & (m.object == '검출력 이슈가') & (m.predicate == '발생 했다'))
    def categoryCrackInsp(c):
        c.assert_fact({'subject': c.m.subject, 'object': '사용자 정의 검사 항목', 'predicate': '이다'})

    @when_all((m.subject == 'Scratch 검사') & (m.object == '검출력 이슈가') & (m.predicate == '발생 했다'))
    def categoryScratchInsp(c):
        c.assert_fact({'subject': c.m.subject, 'object': '사용자 정의 검사 항목', 'predicate': '이다'})

    @when_all((m.subject == '3D 검사') & (m.object == '검출력 이슈가') & (m.predicate == '발생 했다'))
    def category3DInsp(c):
        c.assert_fact({'subject': c.m.subject, 'object': '사전 정의 검사 항목', 'predicate': '이다'})

    # Recipe 이슈
    @when_all(c.first << (m.object == '검출력 이슈가') & (m.predicate == '발생 했다'),
              (m.object == 'Recipe가') & (m.predicate == '문제 있다') & (m.subject == c.first.subject))
    def categoryModifyRecipe(c):
        c.assert_fact({'subject': c.first.subject, 'object': 'Recipe를', 'predicate': '수정 한다'})

    @when_all((m.object == 'Recipe를') & (m.predicate == '수정 한다'))
    def categoryTestRecipe(c):
        c.assert_fact({'subject': c.m.subject, 'object': '수정된 Recipe를', 'predicate': 'Test 한다'})

    @when_all((m.object == 'Recipe를') & (m.predicate == 'Test 한다'))
    def categoryApplyRecipe(c):
        c.assert_fact({'subject': c.m.subject, 'object': '수정된 Recipe를', 'predicate': '현장에 적용한다'})

    # 알고리즘 이슈
    @when_all(c.first << (m.object == '검출력 이슈가') & (m.predicate == '발생 했다'),
              (m.object == 'Recipe가') & (m.predicate == '문제 없다') & (m.subject == c.first.subject))
    def categoryModifyAlgo(c):
        c.assert_fact({'subject': c.first.subject, 'object': '알고리즘을', 'predicate': '수정 한다'})

    @when_all((m.object == '알고리즘을') & (m.predicate == '수정 한다'))
    def categoryTestAlgo(c):
        c.assert_fact({'subject': c.m.subject, 'object': '수정된 알고리즘을', 'predicate': 'Test 한다'})

    @when_all(c.first << (m.object == '수정된 알고리즘을') & (m.predicate == 'Test 한다'),
              (m.object == '사전 정의 검사 항목') & (m.predicate == '이다') & (m.subject == c.first.subject))
    def categoryApplyPredefineAlgo(c):
        c.assert_fact({'subject': c.first.subject, 'object': '알고리즘을', 'predicate': '현장에 적용 한다'})

    @when_all(c.first << (m.object == '수정된 알고리즘을') & (m.predicate == 'Test 한다'),
              (m.object == '사용자 정의 검사 항목') & (m.predicate == '이다') & (m.subject == c.first.subject))
    def categoryTestUserDefineAlgo(c):
        c.assert_fact({'subject': c.first.subject, 'object': '다른 사용자 정의 항목도', 'predicate': 'Test 한다'})

    @when_all((m.object == '다른 사용자 정의 항목도') & (m.predicate == 'Test 한다'))
    def categoryApplyAlgo(c):
        c.assert_fact({'subject': c.m.subject, 'object': '수정된 알고리즘을', 'predicate': '현장에 적용 한다'})

    # Scale 이슈
    @when_all(c.first << (m.object == '검출력 이슈가') & (m.predicate == '발생 했다'),
        (m.object == 'Recipe와 알고리즘에') & (m.predicate == '문제 없다') & (m.subject == c.first.subject))
    def categorySacle(c):
        c.assert_fact({'subject': c.first.subject, 'object': 'Scale을', 'predicate': '확인 한다'})

    @when_all(c.first << (m.object == 'Scale을') & (m.predicate == '확인 한다'),
              (m.object == 'Scale에') & (m.predicate == '문제 없다') & (m.subject == c.first.subject))
    def categorySacleIsOK(c):
        c.assert_fact({'subject': c.first.subject, 'object': '검출력 이슈', 'predicate': '원인 파악 불가능'})

    @when_all((m.object == '검출력 이슈') & (m.predicate == '원인 파악 불가능'))
    def categoryOrderAdditionalData(c):
        c.assert_fact({'subject': c.m.subject, 'object': '추가 Data를', 'predicate': '요청 한다'})

    @when_all(c.first << (m.object == 'Scale을') & (m.predicate == '확인 한다'),
              (m.object == 'Scale에') & (m.predicate == '문제 있다') & (m.subject == c.first.subject))
    def categorySacleIsWrong(c):
        c.assert_fact({'subject': 'Scale 보정을', 'object': '현장에', 'predicate': '요청한다'})

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.object, c.m.predicate))


def exitByOutOfRange():
    print('입력 가능한 범위 초과')
    exit(0)

inspectionItemType = int( input("Issue Item [Ball(1)],[Land(2)],[Crack(3)],[Scratch(4)],[3D(5)] :"))
inspectionItemName = str
if inspectionItemType == 1:
    inspectionItemName = 'Ball 검사'
elif inspectionItemType == 2:
    inspectionItemName = 'Land 검사'
elif inspectionItemType == 3:
    inspectionItemName = 'Crack 검사'
elif inspectionItemType == 4:
    inspectionItemName = 'Scratch 검사'
elif inspectionItemType == 5:
    inspectionItemName = '3D 검사'
else:
    exitByOutOfRange()

recipeAndAlgoIssueType = int( input("Recpie & 알고리즘 [Recipe 이상 없음(1)],[Recipe 이상(2)],[Recipe와 알고리즘 이상 없음(3)] :"))
recipeAndAlgoIssueTitle = 'Recipe가'
recipeAndAlgoIssueIsOK = str
if recipeAndAlgoIssueType == 1:
    recipeAndAlgoIssueIsOK = '문제 없다'
elif recipeAndAlgoIssueType == 2:
    recipeAndAlgoIssueIsOK = '문제 있다'
elif recipeAndAlgoIssueType == 3:
    recipeAndAlgoIssueTitle = 'Recipe와 알고리즘에'
    recipeAndAlgoIssueIsOK = '문제 없다'
else:
    exitByOutOfRange()

scaleIssueType = int
scaleObjectIssue = str
if recipeAndAlgoIssueType == 3:
    scaleIssueType = int( input("Scale 관련 [Scale 이상 없음(1)],[Scale 이상(2)] :"))

    if scaleIssueType == 1:
        scaleObjectIssue = '문제 없다'
    elif scaleIssueType == 2:
        scaleObjectIssue = '문제 있다'
    else:
        exitByOutOfRange()


assert_fact('Solution', { 'subject': inspectionItemName, 'object': '검출력 이슈가', 'predicate': '발생 했다' })
assert_fact('Solution', { 'subject': inspectionItemName, 'object': recipeAndAlgoIssueTitle, 'predicate': recipeAndAlgoIssueIsOK })
if recipeAndAlgoIssueType == 3:
    assert_fact('Solution', {'subject': inspectionItemName, 'object': 'Scale에', 'predicate': scaleObjectIssue})
