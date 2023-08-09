<template>
  <div class="tab">
    <input type="radio" name="css-tabs" :id="tab_id" checked class="tab-switch">
    <label :for="tab_id" class="tab-label">{{ tab_name }}</label>
    <div class="tab-content">
    </div>
  </div>
</template>

<script>
export default {
  name: "MyTab",
  props: {
    tab_name: String,
    tab_id: String
  }
}
</script>

<style scoped>
.tab {
  height: 10vw;
  width: 25%;
  background-color: #404743;
  /*float: left;*/
}


.tab-switch {
  display: none;
}
.tab-label {
  width: 100%;
  /*position: relative;*/
  /*display: block;*/
  /*line-height: 2.75em;*/
  height: 3vw;
  padding: 0 1.618em;
  /*background: #03E069;*/
  /*border-right: 0.125rem solid #16a085;*/
  color: #03E069;
  cursor: pointer;
  top: 0;
  transition: all 0.25s;
}
.tab-label:hover {
  top: -0.25rem;
  transition: top 0.25s;
}
.tab-content {
  height: 12rem;
  /*position: absolute;*/
  z-index: 1;
  top: 2.75em;
  left: 0;
  padding: 1.618rem;
  background: #282c2a;
  color: #2c3e50;
  border-bottom: 0.25rem solid #bdc3c7;
  opacity: 0;
  transition: all 0.35s;
}
.tab-switch:checked + .tab-label {
  background: #03E069;
  color: #404743;
  border-bottom: 0;
  border-right: 0.125rem solid #fff;
  transition: all 0.35s;
  z-index: 1;
  top: -0.0625rem;
}
.tab-switch:checked + label + .tab-content {
  z-index: 2;
  opacity: 1;
  transition: all 0.35s;
}
</style>