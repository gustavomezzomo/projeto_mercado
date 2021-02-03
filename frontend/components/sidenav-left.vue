<template>
  <v-navigation-drawer class="orange accent-2" dark fixed v-model="state.drawer" app>
    <v-list dense>
      <v-list-item @click.stop="state.left = !state.left">
        <v-flex xs4 justify-center align-center>
          <v-btn color="rgb(255,0,0)" icon-color="white" href="/" target="blank">
            <v-list-item-action>
              <v-icon>mdi-home</v-icon>
            </v-list-item-action>
          </v-btn>
          <pre>
<v-btn color="rgb(255,0,0)" icon-color="white" href="/setores" target="blank">
            <v-list-item-action>
              <v-icon>mdi-shopping</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Nossos Setores!</v-list-item-title>
            </v-list-item-content>
          </v-btn>
        </pre>
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
