<template>
  <v-navigation-drawer class="orange accent-2" :width="320" dark v-model="state.drawer" app>
    <v-list dense>
      <v-list-item class="justify-space-around" @click.stop="state.left = !state.left">
        <v-flex xs4>
          <v-btn class="my-2" color="rgb(255,0,0)" icon-color="white" href="/" target="blank">
            <v-list-item-action>
              <v-icon>mdi-home</v-icon>
            </v-list-item-action>
          </v-btn>
          <v-btn color="rgb(255,0,0)" icon-color="white" href="/setores" target="blank">
            <v-list-item-action>
              <v-icon>mdi-shopping</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Nossos Setores!</v-list-item-title>
            </v-list-item-content>
          </v-btn>
        </v-flex>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: ['state']
}
</script>
