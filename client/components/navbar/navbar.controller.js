'use strict';

class NavbarController {
  constructor($location) {
    this.$location = $location;
    this.$el = angular.element("#navbar");
    this.main = angular.element("#main");
    this.active = false;
  }

  toggleSidebar() {
    this.active = !this.active;
    if(this.active){
      this.$el.addClass("active");
      this.main.addClass("active");
    }
    else{
      this.$el.removeClass("active");
      this.main.removeClass("active");
    }
  }

  goHome() {
    this.$location.path("/")
  }
}

angular.module('shiternetApp')
  .controller('NavbarController', NavbarController);
