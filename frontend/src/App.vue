<template>
  <div>
    <textarea id="random-id" cols="30" rows="10" placeholder="Введите текст" v-model="text"></textarea>
    <input type="file" ref="file">
    <button @click="sentToBackend">отправить на бэк</button>
  </div>
  <div class="app">
    <button @click="getPosts">Получить посты</button>
  </div>
</template>


<script>
import axios from 'axios';

export default {
    methods: {
        async getPosts() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/test-task/');
                console.log(response)
            } catch (error) {
                console.error(error)
            }
        },
        async sentToBackend() {
            const file = this.$refs.file.files[0]; // Получаем выбранный файл
            const reader = new FileReader();
            reader.onload = e => {
                const base64Data = reader.result; // Преобразуем файл в base64
                // Отправляем данные на бэкенд
                axios.post('http://127.0.0.1:8000/api/test-task/', {
                    text: this.text, // Текст из textarea
                    picture: base64Data // Данные изображения в формате base64
                });
            };
            const blob = new Blob([file], {type: file.type});
            reader.readAsDataURL(blob); // Читаем файл как data URL
        }
    }
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.app {
    padding: 15px;
    border: 3px solid teal;
}
</style>
