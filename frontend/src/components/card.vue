<template>


  <div class="card_block">

    <div class="card_border">

      <div class="card_content">
        <p class="card_header">{{ header }}</p>
        <a target="_blank" :href=special_text.href class="card_special_text" v-if=special_text>{{ special_text.text }}</a>
        <p class="card_description">{{ description }}</p>
        <a class="card_url" target="_blank" :href=url.href v-if=url>{{ url.text }}</a>
        <code class="card_code" v-if=code>{{ code }}</code>
      </div>
      <a class="github_url" :href=github target="_blank">
        <svg class="card_github" xmlns="http://www.w3.org/2000/svg" width="51" height="51" viewBox="0 0 51 51"
             fill="none">
          <path fill-rule="evenodd" clip-rule="evenodd"
                d="M25.569 0.56897C11.7637 0.56897 0.568848 12.0446 0.568848 26.2017C0.568848 37.5271 7.73217 47.1355 17.6655 50.5249C18.915 50.7622 19.3737 49.9689 19.3737 49.2918C19.3737 48.6806 19.3505 46.6614 19.3397 44.5195C12.3846 46.0701 10.917 41.4951 10.917 41.4951C9.77978 38.5323 8.14119 37.7444 8.14119 37.7444C5.87292 36.1535 8.31218 36.1862 8.31218 36.1862C10.8226 36.3666 12.1445 38.8277 12.1445 38.8277C14.3743 42.7465 17.993 41.6135 19.4196 40.9585C19.644 39.3023 20.2919 38.1706 21.0068 37.5309C15.454 36.8828 9.61666 34.6848 9.61666 24.8629C9.61666 22.0643 10.5933 19.7777 12.1925 17.9826C11.9329 17.3365 11.0772 14.7298 12.4347 11.1991C12.4347 11.1991 14.534 10.5102 19.3116 13.8266C21.3058 13.2587 23.4445 12.9738 25.569 12.9641C27.6937 12.9738 29.834 13.2587 31.8319 13.8266C36.6036 10.5102 38.7001 11.1991 38.7001 11.1991C40.0609 14.7298 39.2047 17.3365 38.9452 17.9826C40.5481 19.7777 41.5182 22.0643 41.5182 24.8629C41.5182 34.7082 35.6697 36.8759 30.1027 37.5105C30.9994 38.306 31.7984 39.866 31.7984 42.2575C31.7984 45.6867 31.7694 48.4471 31.7694 49.2918C31.7694 49.9739 32.2194 50.7732 33.4867 50.5215C43.4146 47.1283 50.5688 37.5232 50.5688 26.2017C50.5688 12.0446 39.3757 0.56897 25.569 0.56897Z"
                fill="#D3ACCC"/>
        </svg>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectCard',
  props: {
    type: String,
    selected_tab: String,
    header: String,
    description: String,
    url: Object,
    code: String,
    special_text: String,
    github: String,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card_border {
  width: 90%;
  height: 95%;
  z-index: 2;

  border-top: 1px solid #C32A7C;
  border-left: 1px solid #C32A7C;

  border-radius: 2vw 0 0 0;

  display: flex;
  flex-direction: column;
  justify-content: space-between;

  color: #DDCFE1;
  font-family: 'Source Code Pro', monospace;

}

.card_content {
  width: 110%;
}

.card_header {
  font-size: 2vh;
  margin: 0;
  font-weight: 600;
  padding: 1vh 0;
}

.card_description {
  font-size: 1.6vh;
  margin: 0;
  font-weight: 400;
  padding: 1vh;
}

.card_special_text {
  color: #FFF4BB;
  text-decoration: none;
}

.card_url, .card_code {
  color: #1EA4F0;
  font-family: 'Source Code Pro', monospace;

  text-decoration: none;
  font-size: 1.6vh;
  margin: 0;
  font-weight: 400;
  padding: 1vh;
}

.card_block {
  margin: 3% 2%;
  width: 25vh;
  height: 40vh;

  z-index: 2;
  border-radius: 2vw;

  background: linear-gradient(0deg, #120A1B 0%, #120A1B 100%);
  box-shadow: 5px 5px 28px -15px rgba(195, 42, 124, 0.55);
}

.github_url {
  width: 100%;

  display: flex;
  justify-content: start;
}

.card_github {

  margin: 0 1vh;
  /*position: absolute;*/
  /*z-index: 0;*/

  /*margin-top: -3vh;*/
  /*margin-right: -20%;*/

}

</style>
