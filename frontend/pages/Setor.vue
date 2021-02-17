<template>
  <div>
    <div v-show="pending"> CARREGANDO </div>
    <div v-show="!pending">
      <v-layout justify-center align-center class="red--text">
        <h2>{{setor.title}}</h2>
      </v-layout>
      <v-divider class="centraliza" />
      <div v-for="item in products" v-bind="products" :key="item.title">
        <h1 class="red--text">{{item.title}}</h1>
        <v-layout>
          <v-img
            max-height="100%"
            max-width="500"
            :src="product.image"
          />
        </v-layout>
      </div>
    </div>
  </div>
</template>

<script>

import api from '~/components/api/api.js'

export default {
  data () {
    return {products: [{title: 'example'}],
      setor: {title: 'padrao'},
      pending: true,
      image
      }
    }
  }
  mounted () ;{
    this.pending = true
    api.list_products_by_setor(this.$route.params.slug)
      .then(result => {
        this.products = result.products
        this.setor = result.setor
        this.pending = false
      }),
    api.image().then (result => {
        this.product = result
  },
</script>

<style>
  .centraliza {
    padding: 8px;
  }
</style>
