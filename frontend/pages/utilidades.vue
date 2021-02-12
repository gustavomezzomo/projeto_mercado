<template>
  <div>
    <v-layout justify-center align-center class="red--text">
      <h2>UTILIDADES</h2>
    </v-layout>
    <v-divider class="centraliza" />
    <v-layout justify-center align-center>
      <v-img
        max-height="100%"
        max-width="500"
        :src="postAtual.image"
      />
    </v-layout>
  </div>
</template>

<script>

import api from '~/components/api/api.js'

export default {
  data () {
    return {postAtual: {

    }

    }
  },
  mounted () {
    api.image().then(result => {
      this.postAtual = result
    })
  }
}
</script>

<style>
  .centraliza {
    padding: 8px;
  }
</style>
