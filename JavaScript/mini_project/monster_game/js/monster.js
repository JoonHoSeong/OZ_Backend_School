let monsterHP = 100
const h1 = document.createElement("h1")
h1.textContent = "몬스터 잡기 게임을 시작합니다!"
document.body.appendChild(h1)

let attackDamage = parseInt(prompt("1회 공격 시 데미지는 얼마인가요? (양의 정수로 입력하세요)"))
let attackCount = 0

if(attackDamage > 0){

  let p;

  while(monsterHP > 0){
    attackCount += 1
    monsterHP -= attackDamage

    p = document.createElement("p")
    p.textContent = `몬스터를 ${attackCount}회 공격했습니다!`
    document.body.appendChild(p)

    if (monsterHP<0){
        monsterHP = 0;
    }
    strong = document.createElement("strong")
    strong.textContent = `몬스터의 남은 HP는 ${monsterHP}입니다!`
    document.body.appendChild(strong)
  }

  h2 = document.createElement("h2")
  h2.textContent = "몬스터 잡기 완료! 수고하셨습니다."
  h2.style.color = "orange"
  h2.title = '게임을 다시 시작하고 싶으면 새로고침을 하세요.'
  document.body.appendChild(h2)


}else{
  alert("데미지를 잘못 입력하여 게임을 취소합니다!")
}