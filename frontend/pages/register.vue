<template>
  <div
    class="RegisterPageCard flex flex-col-reverse xl:flex-row gap-5 overflow-hidden"
  >
    <!------------ left section ------------>
    <div
      class="w-full xl:w-1/2 bg-slate-800 rounded-[40px] sm:px-16 sm:py-10 p-6 animate__animated animate__zoomIn"
    >
      <h2
        class="font-m mb-5 sm:mb-12 text-center animate__animated animate__bounceInDown"
      >
        Register
      </h2>
      <!------------ input fields ------------>
      <BaseTextInput
        inputName="email"
        title="Email"
        type="text"
        placeholder="example@gmail.com"
        class="mb-4 sm:mb-10 animate__animated animate__bounceInLeft"
      />
      <BaseTextInput
        inputName="password"
        title="Password"
        type="password"
        placeholder="Password"
        class="mb-4 sm:mb-10 animate__animated animate__bounceInLeft"
      />
      <BaseTextInput
        inputName="agreed"
        title="Confirm password"
        type="password"
        placeholder="Password confirm"
        class="mb-5 sm:mb-12 animate__animated animate__bounceInLeft"
      />
      <!------------ login or register buttons ------------>
      <div
        class="flex w-full justify-center animate__animated animate__bounceInUp"
      >
        <BaseButtonGroup
          leftButtonText="Register"
          rightButtonText="Login"
          @on-right-button-click="navigateTo('/login')"
        />
      </div>
    </div>
    <!------------ right section ------------>
    <div class="w-full xl:w-1/2 mb-5 xl:mb-0">
      <h1
        class="max-w-[200px] sm:max-w-md text-center mb-5 mx-auto animate__animated animate__bounceInDown"
      >
        Custom web news website
      </h1>
      <div class="flex w-full xl:h-[600px] justify-center items-center">
        <img
          src="/_nuxt/assets/images/man1.webp"
          alt=""
          class="w-5/12 animate__animated animate__zoomIn"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  layout: "auth-layout",
});
</script>
