let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

canvas.width = 650;
canvas.height = 200;
////////////////////////////////////////////////////
window.addEventListener('load', init);

let words = [
    'America', 'Brazil', 'Canada', 'Denmark', 'Egypt', 'Finland', 
    'Germany', 'Hungary', 'Italy', 'Jordan', 'Korea', 'Lebanon', 
    'Mexico', 'Norway', 'Oman', 'Panama', 'Qatar', 'Romania', 
    'Sweden', 'Thailand', 'Ukraine', 'Venezuela', 'Wallis', 'Yemen', 'Zambia' ];

// DOM Elements
const wordInput = document.querySelector('#word-input');
const currentWord = document.querySelector('#current-word');

let isPlaying;
let checkWord;
let count_word = 0;

// Pick & show random word
function showWord(words) {
    // Generate random array index
    const randIndex = Math.floor(Math.random() * words.length);
    // Output random word
    currentWord.innerHTML = words[randIndex];
}

// Match currentWord to wordInput
function matchWords() {
    if (wordInput.value === currentWord.innerHTML) {
      checkWord = true;
      count_word = count_word + 1;
      return checkWord;
    } else {
      checkWord = false;
      return checkWord;
    }
}

// Start match
function startMatch() {

    if (matchWords()) {
      isPlaying = true;
      showWord(words);
      wordInput.value = '';
    } else {
        isPlaying = false;
    }
}

function init() {
    showWord(words);
    wordInput.addEventListener('input', startMatch);
}

//////////////////////////////////////////////////////
let enemy;
let enemies = [];
let player;
let element = document.documentElement;
let game_speed;
let count_score;
let score;
const speed_bg = 0.5;


let keyboard_input = {
    up:false,
    space:false,
    open_full:false,
    close_full:false,
    jumping:false,

    keyListener:function (event) {
        var key_state = (event.type == "keydown")?true:false;
        switch (event.keyCode) {

            case 38: // arrow up button
                keyboard_input.up = key_state;
            break;
            case 33: // page up button
                keyboard_input.open_full = key_state;
            break;
            case 27: // Esc button
                keyboard_input.close_full = key_state;
            break;
            case 13:
                if (isPlaying) {
                    keyboard_input.jumping = key_state;
                }
            break;
        }
    }
}

sprite_sheet = {
    frame_sets:[[0, 1]],
    image:new Image()
};

enemy_sheet = new Image();

background = new Image();
bg = {
    x1 : 0,
    x2 : canvas.width,
    y : 0,
    width : canvas.width,
    height : canvas.height
}

class Player {

    constructor (frame_set, speed) {
        this.x = 25;
        this.y = 0;
        this.w = 50;
        this.h = 50;
        this.dist_y = 0;
        this.count = 0;
        this.speed = speed;
        this.frame = 0;
        this.frame_index = 0;
        this.frame_set = frame_set;
    }


    jump () {
        if (this.y == canvas.height - this.h) {
            this.dist_y = -9;
        }
    }

    show () {
        context.drawImage(sprite_sheet.image, this.frame * this.h , 0, 
            this.w, this.h, this.x, this.y, this.w, this.h);
    }

    control () {
        if (keyboard_input.jumping) {
            this.jump();
        }

        this.y += this.dist_y;

        if (this.y + this.h < canvas.height) {
            this.dist_y += 0.15;
        } else {
            this.dist_y = 0;
            this.y = canvas.height - this.h;
        }

        this.show();
    }

 
    change(frame_set,speed){
        if (this.frame_set != frame_set) {
            this.count = 0;
            this.speed = speed;
            this.frame_index = 0;
            this.frame_set = frame_set;
            this.frame = this.frame_set[this.frame_index];
    
          }
    }

    update(){
        this.count ++;
      if (this.count >= this.speed) {
        this.count = 0;
        this.frame_index = (this.frame_index == this.frame_set.length - 1) ? 0 : this.frame_index + 1;
        this.frame = this.frame_set[this.frame_index];
      }
    }

}

class Enemy {

    constructor (x,rand_enemy) {
        this.x = x;
        this.y = 150;
        this.w = 50;
        this.h = 50;
        this.dist_x = -game_speed;
        this.rand_enemy = rand_enemy;
    }

    show () {
        context.drawImage(enemy_sheet, this.rand_enemy , 0, this.w, this.h, this.x, this.y, this.w, this.h);
    }

    run () {
        this.x += this.dist_x;
        this.show();
        this.dist_x = -game_speed;
    }

}

class Score {

    constructor (score) {;
        this.text = "Score : " + score;
        this.x = 325;
        this.y = 40;
        this.align = "center";
    }

    show () {
        context.fillStyle = 'black';
        context.font = "20px Consolas";
        context.textAlign = this.align;
        context.fillText(this.text, this.x, this.y);
    }
}

function random_dist (min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

function random_enemy(){
    return Math.round(Math.random() * 13) * 50; // frame size 700*50 
}

function spawn_enemy () {
    let x_pos = random_dist(canvas.width, canvas.width + 350);
    let rand_enemy = random_enemy();
    enemy = new Enemy(x_pos, rand_enemy);
    enemies.push(enemy);
}

function start () {
    game_speed = 1.5;
    context.font = "20px Consolas";
    score = 0;
    count_score = new Score(score);
    player = new Player();
    requestAnimationFrame(update);
}

function handlebackground (){
    if (bg.x1 <= -bg.width){
        bg.x1 = bg.width;
    }
    else {
        bg.x1 -= speed_bg;
    }
    if (bg.x2 <= -bg.width) {
        bg.x2 = bg.width;
    }
    else {
        bg.x2 -= speed_bg;
    }
    context.drawImage(background, bg.x1, bg.y, bg.width, bg.height);
    context.drawImage(background, bg.x2, bg.y, bg.width, bg.height);
}

let initialSpawnTimer = 500;
let spawnTimer = initialSpawnTimer;
function update () {
    requestAnimationFrame(update);
    handlebackground();
    // context.drawImage(background_sheet.image, 0, 0, canvas.width, canvas.height)
    // context.clearRect(0, 0, canvas.width, canvas.height);
    spawnTimer--;
    if (spawnTimer <= 0) {
        spawn_enemy();
        console.log(enemies);
        spawnTimer = initialSpawnTimer - game_speed * 9;
    
        if (spawnTimer < 60) {
            spawnTimer = 60;
        }
    }

    for (let i = 0; i < enemies.length; i++) {
        let e = enemies[i];

        if (e.x + e.w < 0) {
            enemies.splice(i, 1);
        }

        if (player.x < e.x + e.w && player.x + player.w > e.x && player.y < e.y + e.h && player.y + player.h > e.y) {
                if (confirm("Game Over! \nDo you want to restart?")) {
                    // Case Game Over!!
                    enemies = [];
                    spawnTimer = initialSpawnTimer;
                    game_speed = 1.5;
                    score = 0;
                } else {
                    window.close();
                }
            }
        e.run();
    }

    game_speed += 0.0008;

    if(!player.control()){
        player.change(sprite_sheet.frame_sets[0], 20);
    }

    player.control();
    
    if (keyboard_input.open_full) {
        element.requestFullscreen();
    } else if (keyboard_input.close_full) {
        document.exitFullscreen();
    }

    player.update();
    
    score = count_word;
    count_score.text = "Score : " + score;
    count_score.show();

}

document.addEventListener("keydown", keyboard_input.keyListener);
document.addEventListener("keyup", keyboard_input.keyListener);

requestAnimationFrame(update);


sprite_sheet.image.src = "spiderman.png";
enemy_sheet.src = "sum_enemy.png";
background.src = 'bg01.jpg';



start();