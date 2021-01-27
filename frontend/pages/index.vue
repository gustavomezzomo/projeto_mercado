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

import AppApi from '~apijs'

asyncData(); {
  return AppApi.image().then(result => {
    element.image = 'media/'
  })
  return {
    items: result.data.data
  }
}

export default {
  data () {
    return {}
  }
}
</script>

<style>
  .centraliza {
    padding: 8px;
  }
</style>
