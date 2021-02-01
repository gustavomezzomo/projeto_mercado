<template>
  <v-footer color="rgb(255,0,0)" class="yellow--text" max-height="40" app>
    <v-layout justify-center align-center>
      <span>Mercado Santa Inês - Rua José Alves de Paiva 301 - Santa Inês 2</span>
      <v-btn icon color="yellow" href="https://www.google.com.br/maps/place/Mercado+Santa+Ines/@-23.1666265,-45.8064849,17z/data=!3m1!4b1!4m5!3m4!1s0x94cc4c412d8a682d:0x8f5a9f1e0466af5d!8m2!3d-23.1666265!4d-45.8042962" target="_blank">
        <v-icon>mdi-google-maps</v-icon>
      </v-btn>
    </v-layout>
  </v-footer>
</template>

<script>
export default {
  props: ['state']
}
</script>
