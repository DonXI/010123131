let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

canvas.width = 1300;
canvas.height = 400;

  const SPRITE_SIZE = 27;

  var Animation = function(frame_set, speed) {

    this.count = 0;
    this.speed = speed;
    this.frame = 0;
    this.frame_index = 0;
    this.frame_set = frame_set;

  };

  Animation.prototype = {
    change:function(frame_set, speed) {
      if (this.frame_set != frame_set) {
        this.count = 0;
        this.speed = speed;
        this.frame_index = 0;
        this.frame_set = frame_set;
        this.frame = this.frame_set[this.frame_index];

      }

    },

    update:function() {

      this.count ++;

      if (this.count >= this.speed) {

        this.count = 0;
        this.frame_index = (this.frame_index == this.frame_set.length - 1) ? 0 : this.frame_index + 1;
        this.frame = this.frame_set[this.frame_index];

      }

    }

  };

  var buffer, controller, display, loop, player, render, resize, sprite_sheet;

  buffer = document.createElement("canvas").getContext("2d");
  display = document.querySelector("canvas").getContext("2d");


  controller = {
    up:    { active:false, state:false },
    open_full:{ active:false, state:false },
    close_full:{ active:false, state:false },
    keyUpDown:function(event) {
      var key_state = (event.type == "keydown") ? true : false;

      switch(event.keyCode) {
        case 38:// up key
          if (controller.up.state != key_state) controller.up.active = key_state;
          controller.up.state  = key_state;
        break;

        case 33:
          controller.open_full = key_state;
        break;

        case 27:
          controller.close_full = key_state;
        break;
      }
    }
  };

  player = {
    animation:new Animation(),
    jumping:true,
    height:27,    width:27,
    x:0,          y:0,
    x_velocity:0, y_velocity:0
  };

  sprite_sheet = {
    frame_sets:[[0, 1]],
    image:new Image()

  };


  var element = document.documentElement;
  loop = function(time_stamp) {

    if (controller.up.active && !player.jumping) {
      controller.up.active = false;
      player.jumping = true;
      player.y_velocity -= 5;

    }
    if(!controller.up.active){
      console.log("show_animation")
      player.animation.change(sprite_sheet.frame_sets[0], 10);//เรียกใช้ animation , ความเร็วในการเล่น animation
    }
/*
    if (controller.open_full){
      element.requestFullscreen();
    }
    else if (controller.close_full){
      element.exitFullscreen();
    }
    */

    player.y_velocity += 0.25;
    player.y += player.y_velocity;
    player.y_velocity *= 1;

    if (player.y + player.height > buffer.canvas.height) {
      player.jumping = false;
      player.y = buffer.canvas.height - player.height;
      player.y_velocity = 0;

    } 

    player.animation.update();
    buffer.fillStyle = "pink";
    buffer.fillRect(0, 0, buffer.canvas.width, buffer.canvas.height);

    buffer.drawImage(sprite_sheet.image, player.animation.frame * SPRITE_SIZE, 0, SPRITE_SIZE, SPRITE_SIZE, Math.floor(player.x), Math.floor(player.y), SPRITE_SIZE, SPRITE_SIZE);
    display.drawImage(buffer.canvas, 0, 0, buffer.canvas.width, buffer.canvas.height, 0, 0, display.canvas.width, display.canvas.height);

    window.requestAnimationFrame(loop);

  };


  buffer.canvas.width = 400;
  buffer.canvas.height = 110;


  window.addEventListener("keydown", controller.keyUpDown);
  window.addEventListener("keyup", controller.keyUpDown);


  sprite_sheet.image.addEventListener("load", function(event) {
    window.requestAnimationFrame(loop);
  });

  sprite_sheet.image.src = "sp_50x27_ver03.png";

