<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  
  <button
    :style="buttonStyle"
    @click="handleCick"
  >
    클릭하세요
  </button>
  
  <!-- 3x4 표 추가 -->
  <table
    style="margin-top: 30px; width: 60%; margin-left: auto; margin-right: auto; border: 1px solid #ddd; border-collapse: collapse;"
    @click="toggllColor"
  >
    <thead>
      <tr>
        <th style="padding: 8px; border: 1px solid #ddd; text-align: center;">헤더 1</th>
        <th style="padding: 8px; border: 1px solid #ddd; text-align: center;">헤더 2</th>
        <th style="padding: 8px; border: 1px solid #ddd; text-align: center;">헤더 3</th>
        <th style="padding: 8px; border: 1px solid #ddd; text-align: center;">헤더 4</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td v-for="(col, colIndex) in columns" :key="'row1-' + colIndex" style="padding: 8px; border: 1px solid #ddd; text-align: center;">데이터 1-{{col}}</td>
      </tr>
      <tr>
        <td v-for="(col, colIndex) in columns" :key="'row2-' + colIndex" style="padding: 8px; border: 1px solid #ddd; text-align: center;">데이터 2-{{col}}</td>
      </tr>
      <tr>
        <td v-for="(col, colIndex) in columns" :key="'row3-' + colIndex" style="padding: 8px; border: 1px solid #ddd; text-align: center;">데이터 3-{{col}}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data() {
    return {
      isClicked: false,
      columns: [1, 2, 3, 4], // 열 번호 (데이터의 표시 순서)
      clickedCells: [] // 클릭된 셀의 상태를 추적
    }
  },
  computed: {
    buttonStyle() {
      return {
        width: '77px',
        height: '40px',
        backgroundColor: this.isClicked ? 'lightgreen' : 'darkpurple',
        color: 'white',
        border: 'none',
        cursor: 'pointer',
        fontSize: '14px',
        borderRadius: '5px'
      }
    }
  },
  methods: {
    handleClick() {
      if (!this.isClicked) {
        alert('버튼입니다');
        this.isClicked = true;
      } else {
        this.isClicked = false;
      }
    },
    toggleCellColor(event) {
      // 클릭된 셀을 찾아서 색을 반전시킴
      const cell = event.target;
      if (cell.tagName === 'TD') {
        const isClicked = this.clickedCells.includes(cell);
        if (isClicked) {
          cell.style.backgroundColor = ''; // 색상 초기화
          this.clickedCells = this.clickedCells.filter(c => c !== cell);
        } else {
          cell.style.backgroundColor = 'black'; // 색상 반전
          this.clickedCells.push(cell);
        }
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
