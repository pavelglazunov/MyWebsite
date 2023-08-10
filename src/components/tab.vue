<template>
  <div class="tab-2">
    <label :for="tab_id">{{ tab_name }}</label>
    <input :id="tab_id" name="tabs-two" type="radio" :checked="tab_checked">
  </div>
</template>

<script>
export default {
  name: "MyTab",
  props: {
    tab_name: String,
    tab_id: String,
    tab_checked: Boolean
  },
  methods: {
    emitChange() {
      this.$emit('change', this.tab_id);
    }
  }
}
</script>

<style scoped>


.tabs [class^="tab"] label,
.tabs [class*=" tab"] label {
  color: #efedef;
  cursor: pointer;
  display: block;
  font-size: 1.1em;
  font-weight: 300;
  line-height: 1em;
  padding: 1vh 0;
  /*padding: 2rem 0;*/
  text-align: center;
}

.tabs [class^="tab"] [type="radio"],
.tabs [class*=" tab"] [type="radio"] {
  border-bottom: 1px solid rgba(239, 237, 239, 0.5);
  cursor: pointer;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  display: block;
  width: 100%;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

.tabs [class^="tab"] [type="radio"]:hover,
.tabs [class^="tab"] [type="radio"]:focus,
.tabs [class*=" tab"] [type="radio"]:hover,
.tabs [class*=" tab"] [type="radio"]:focus {
  border-bottom: 1px solid #C32A7C;
}

.tabs [class^="tab"] [type="radio"]:checked,
.tabs [class*=" tab"] [type="radio"]:checked {
  border-bottom: 1px solid #C32A7C;
  color: #C32A7C;
}


.tabs [class^="tab"] [type="radio"]:checked + div,
.tabs [class*=" tab"] [type="radio"]:checked + div {
  opacity: 1;
}

.tabs [class^="tab"] [type="radio"] + div,
.tabs [class*=" tab"] [type="radio"] + div {
  display: block;
  opacity: 0;
  padding: 2rem 0;
  width: 90%;
  -webkit-transition: all 0.3s ease-in-out;
  -moz-transition: all 0.3s ease-in-out;
  -o-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
}

.tabs .tab-2 {
  width: 20vh;
  /*width: 20%;*/
}

/*@media screen and (max-width: 1000px) {*/
/*  .tabs .tab-2 {*/
/*    width: 50%;*/
/*  }*/

/*}*/

.tabs .tab-2 [type="radio"] + div {
  width: 200%;
  margin-left: 200%;
}

.tabs .tab-2 [type="radio"]:checked + div {
  margin-left: 0;
}

.tabs .tab-2:last-child [type="radio"] + div {
  margin-left: 100%;
}

.tabs .tab-2:last-child [type="radio"]:checked + div {
  margin-left: -100%;
}

</style>