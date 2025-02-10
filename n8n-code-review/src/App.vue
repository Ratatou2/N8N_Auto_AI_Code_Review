<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <h1>여기에요 여기!</h1>
  <button
    :style="buttonStyle"
    @click="handleClick"
  >
    클릭하세요
  </button>
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
      isClicked: false
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
