<template>
  <div>
    <div v-show="pending" class="red--text"> CARREGANDO </div>
    <div v-show="!pending">
      <v-layout justify-center align-center class="red--text">
        <h1>CONHEÇA NOSSOS SETORES!!</h1>
      </v-layout>
      <v-divider class="centraliza" />
      <v-layout row wrap>
        <v-flex xs12 sm6 md4 class="pa-3" v-for="setor in setores" :key="setor.title">
          <v-layout justify-center>
            <div class="text-center">
              <h2> <a :href="'/setor/'+setor.slug" class="red--text">{{setor.title}}</a></h2>
            </div>
          </v-layout>
          <v-layout justify-center>
            <v-img
              max-height="50%"
              max-width="300"
              :src="setor.image"
            />
          </v-layout>
        </v-flex>
      </v-layout>
    </div>
  </div>
</template>

<script>

import api from '~/components/api/api.js'

export default {
  data () {
    return {setores: []}
  },
  mounted () {
    this.pending = true
    api.list_setor()
      .then(result => {
        this.setores = result.setor
        this.pending = false
      })
  }
}
</script>

<style>
  .centraliza {
    padding: 8px;
  }
  .text-center {
    text-align: center;
  }
</style>
