<template>
  <div class="LoginPageCard flex flex-col xl:flex-row gap-5 overflow-hidden">
    <!------------ left section ------------>
    <div
      class="w-full xl:w-1/2 bg-slate-800 rounded-[40px] sm:px-16 sm:py-10 p-6 flex flex-col justify-between animate__animated animate__zoomIn"
    >
      <h2
        class="font-m mb-5 sm:mb-12 text-center animate__animated animate__bounceInDown"
      >
        Login to your account
      </h2>
      <!------------ input fields ------------>
      <BaseTextInput
        inputName="email"
        title="Email"
        type="text"
        placeholder="example@gmail.com"
        succeed-message="valid nice!"
        class="animate__animated animate__bounceInLeft"
      />
      <BaseTextInput
        inputName="password"
        title="Password"
        type="password"
        placeholder="Password"
        class="mb-3 animate__animated animate__bounceInLeft"
        error-message="wrong password"
      />
      <!------------ login or register buttons ------------>
      <div
        class="flex w-full justify-center animate__animated animate__bounceInUp"
      >
        <BaseButtonGroup leftButtonText="Login" rightButtonText="Register" />
      </div>
    </div>
    <!------------ right section ------------>
    <div
      class="w-full xl:w-1/2 flex flex-col items-center justify-between mb-5 xl:mb-0"
    >
      <h1
        class="max-w-[200px] sm:max-w-md text-center mb-5 animate__animated animate__bounceInDown"
      >
        Custom web news website
      </h1>
      <img
        src="/_nuxt/assets/images/man3.webp"
        alt=""
        class="w-5/12 animate__animated animate__zoomIn"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "auth-layout",
});
</script>
