<template>
  <div>
    <v-layout justify-center align-center class="red--text">
      <h2>PROMOÇÃO DO DIA!</h2>
    </v-layout>
    <v-divider class="centraliza" />
    <v-layout justify-center align-center>
      <v-img
        max-height="100%"
        max-width="500"
        src="element.image"
      />
    </v-layout>
  </div>
</template>

<script>

import api from '~/components/api/api.js'

export default {
  data () {
    return {

    }
  },
  mounted () {
    let retorno = {}
    // eslint-disable-next-line no-debugger
    debugger
    api.image().then(result => {
      // result.image = 'media/'
      retorno = result
    })
    return {
      items: retorno.data.data
    }
  }
}
</script>

<style>
  .centraliza {
    padding: 8px;
  }
</style>
