<template>
  <div class="carousel my-carousel carousel--translate">
    <input class="carousel__activator" type="radio" name="carousel" id="F" checked="checked"/>
    <input class="carousel__activator" type="radio" name="carousel" id="G"/>
<!--    <input class="carousel__activator" type="radio" name="carousel" id="H"/>-->
<!--    <input class="carousel__activator" type="radio" name="carousel" id="I"/>-->
<!--    <input class="carousel__activator" type="radio" name="carousel" id="J"/>-->
    <div class="carousel__controls">
      <label class="carousel__control carousel__control--backward" for="G"></label>
      <label class="carousel__control carousel__control--forward" for="G"></label>
    </div>
    <div class="carousel__controls">
      <label class="carousel__control carousel__control--backward" for="F"></label>
      <label class="carousel__control carousel__control--forward" for="F"></label>
    </div>
<!--    <div class="carousel__controls">-->
<!--      <label class="carousel__control carousel__control&#45;&#45;backward" for="G"></label>-->
<!--      <label class="carousel__control carousel__control&#45;&#45;forward" for="I"></label>-->
<!--    </div>-->
<!--    <div class="carousel__controls">-->
<!--      <label class="carousel__control carousel__control&#45;&#45;backward" for="H"></label>-->
<!--      <label class="carousel__control carousel__control&#45;&#45;forward" for="J"></label>-->
<!--    </div>-->x`
<!--    <div class="carousel__controls">-->
<!--      <label class="carousel__control carousel__control&#45;&#45;backward" for="I"></label>-->
<!--      <label class="carousel__control carousel__control&#45;&#45;forward" for="F"></label>-->
<!--    </div>-->
    <div class="carousel__track">
      <li class="carousel__slide">
        <img class="carousel_image" alt="Image? Where are tou?" src="./../assets/MyImage.png">
      </li>
      <li class="carousel__slide">
        <img class="carousel_image" alt="Image? Where are tou?" src="./../assets/MyImage1.png">
      </li>
<!--      <li class="carousel__slide">-->
<!--        <img class="carousel_image" alt="Image? Where are tou?" src="./../assets/photo_2023-08-11_01-22-23.jpg">-->
<!--      </li>-->
<!--      <li class="carousel__slide">-->
<!--        <h1>G</h1>-->
<!--      </li>-->
<!--      <li class="carousel__slide">-->
<!--        <h1>H</h1>-->
<!--      </li>-->
<!--      <li class="carousel__slide">-->
<!--        <h1>I</h1>-->
<!--      </li>-->
<!--      <li class="carousel__slide">-->
<!--        <h1>J</h1>-->
<!--      </li>-->
    </div>
    <div class="carousel__indicators">
      <label class="carousel__indicator" for="F"></label>
      <label class="carousel__indicator" for="G"></label>
<!--      <label class="carousel__indicator" for="H"></label>-->
<!--      <label class="carousel__indicator" for="I"></label>-->
<!--      <label class="carousel__indicator" for="J"></label>-->
    </div>
  </div>
</template>

<script>
export default {
  name: "CarouselImage"
}
</script>

<style scoped>

.carousel_image {
  width: 100%;
  height: 100%;
  border-radius: 1vw;

}

.carousel {
  height: 100%;
  width: 100%;
  overflow: hidden;
  text-align: center;
  position: relative;
  padding: 0;
  list-style: none;
  box-shadow: 0px 0px 250px -2px rgba(235, 37, 86, 0.25);
  border-radius: 1vw;

  transition-duration: 0.3s;

}
.carousel:hover {
  box-shadow: 0px 0px 250px -2px rgba(235, 37, 86, 0.3);
}


.carousel__controls,
.carousel__activator {
  display: none;
}

.carousel__activator:nth-of-type(1):checked ~ .carousel__track {
  transform: translateX(0%);
}

.carousel__activator:nth-of-type(1):checked ~ .carousel__slide:nth-of-type(1) {
  transition: opacity 0.5s, transform 0.5s;
  top: 0;
  left: 0;
  right: 0;
  opacity: 1;
  transform: scale(1);
}

.carousel__activator:nth-of-type(1):checked ~ .carousel__controls:nth-of-type(1) {
  display: block;
  opacity: 1;
}

.carousel__activator:nth-of-type(1):checked ~ .carousel__indicators .carousel__indicator:nth-of-type(1) {
  opacity: 1;
}

.carousel__activator:nth-of-type(2):checked ~ .carousel__track {
  transform: translateX(-100%);
}

.carousel__activator:nth-of-type(2):checked ~ .carousel__slide:nth-of-type(2) {
  transition: opacity 0.5s, transform 0.5s;
  top: 0;
  left: 0;
  right: 0;
  opacity: 1;
  transform: scale(1);
}

.carousel__activator:nth-of-type(2):checked ~ .carousel__controls:nth-of-type(2) {
  display: block;
  opacity: 1;
}

.carousel__activator:nth-of-type(2):checked ~ .carousel__indicators .carousel__indicator:nth-of-type(2) {
  opacity: 1;
}

.carousel__activator:nth-of-type(3):checked ~ .carousel__track {
  transform: translateX(-200%);
}

.carousel__activator:nth-of-type(3):checked ~ .carousel__slide:nth-of-type(3) {
  transition: opacity 0.5s, transform 0.5s;
  top: 0;
  left: 0;
  right: 0;
  opacity: 1;
  transform: scale(1);
}

.carousel__activator:nth-of-type(3):checked ~ .carousel__controls:nth-of-type(3) {
  display: block;
  opacity: 1;
}

.carousel__activator:nth-of-type(3):checked ~ .carousel__indicators .carousel__indicator:nth-of-type(3) {
  opacity: 1;
}

.carousel__activator:nth-of-type(4):checked ~ .carousel__track {
  transform: translateX(-300%);
}

.carousel__activator:nth-of-type(4):checked ~ .carousel__slide:nth-of-type(4) {
  transition: opacity 0.5s, transform 0.5s;
  top: 0;
  left: 0;
  right: 0;
  opacity: 1;
  transform: scale(1);
}

.carousel__activator:nth-of-type(4):checked ~ .carousel__controls:nth-of-type(4) {
  display: block;
  opacity: 1;
}

.carousel__activator:nth-of-type(4):checked ~ .carousel__indicators .carousel__indicator:nth-of-type(4) {
  opacity: 1;
}

.carousel__activator:nth-of-type(5):checked ~ .carousel__track {
  transform: translateX(-400%);
}

.carousel__activator:nth-of-type(5):checked ~ .carousel__slide:nth-of-type(5) {
  transition: opacity 0.5s, transform 0.5s;
  top: 0;
  left: 0;
  right: 0;
  opacity: 1;
  transform: scale(1);
}

.carousel__activator:nth-of-type(5):checked ~ .carousel__controls:nth-of-type(5) {
  display: block;
  opacity: 1;
}

.carousel__activator:nth-of-type(5):checked ~ .carousel__indicators .carousel__indicator:nth-of-type(5) {
  opacity: 1;
}

.carousel__control {
  height: 30px;
  width: 30px;
  margin-top: -15px;
  top: 50%;
  position: absolute;
  /*display: block;*/
  cursor: pointer;
  border-width: 5px 5px 0 0;
  border-style: solid;
  border-color: #fafafa;
  opacity: 0.35;
  outline: 0;
  z-index: 3;
}

.carousel__control:hover {
  opacity: 1;
}

.carousel__control--backward {
  left: 10px;
  transform: rotate(-135deg);

  border-color: #C32A7C;


}

.carousel__control--forward {
  right: 10px;
  transform: rotate(45deg);

  border-color: #C32A7C;
}

.carousel__indicators {
  position: absolute;
  bottom: 20px;
  width: 100%;
  text-align: center;
}

.carousel__indicator {
  height: 15px;
  width: 15px;
  border-radius: 100%;
  display: inline-block;
  z-index: 2;
  cursor: pointer;
  opacity: 0.35;
  margin: 0 2.5px 0 2.5px;
}

.carousel__indicator:hover {
  opacity: 0.75;
}

.carousel__track {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 0;
  margin: 0;
  transition: transform 0.5s ease 0s;
}

.carousel__track .carousel__slide {
  display: block;
  top: 0;
  left: 0;
  right: 0;
  opacity: 1;
}

.carousel__track .carousel__slide:nth-of-type(1) {
  transform: translateX(0%);
}

.carousel__track .carousel__slide:nth-of-type(2) {
  transform: translateX(100%);
}

.carousel__track .carousel__slide:nth-of-type(3) {
  transform: translateX(200%);
}

.carousel__track .carousel__slide:nth-of-type(4) {
  transform: translateX(300%);
}

.carousel__track .carousel__slide:nth-of-type(5) {
  transform: translateX(400%);
}

.carousel--scale .carousel__slide {
  transform: scale(0);
}

.carousel__slide {
  height: 100%;
  position: absolute;
  overflow-y: auto;
  opacity: 0;
}

/**
  * Theming
*/
.my-carousel {
  border-radius: 1vw;
}

.carousel__slide {
  overflow: hidden;
}

.carousel__indicator {
  height: 1.3vh;
  width: 1.3vh;
}

.carousel__indicator {
  background-color: #fafafa;
}

</style>