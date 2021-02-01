<template>
  <v-navigation-drawer class="grey accent-2" dark fixed v-model="state.drawer" app>
    <v-list dense>
      <v-list-item @click.stop="state.left = !state.left">
        <v-btn icon-color="white" href="localhost/setores" target="blank">
          <v-list-item-action>
            <v-icon>mdi-shopping</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Nossos Setores!</v-list-item-title>
          </v-list-item-content>
        </v-btn>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  props: ['state']
}
</script>
