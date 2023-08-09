<template>
  <div class="card_block">

  </div>
</template>

<script>
export default {
  name: 'ProjectCard',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card_block {
  width: 20%;
  height: 20vw;

  background-color: #303432;
  border: 1px #03E069 solid;
  border-radius: 2vw;
}
</style>
