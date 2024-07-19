<template>
  <div>
    <textarea id="random-id" cols="30" rows="10"
              placeholder="Введите текст" v-model="text">
    </textarea>
    <input type="file" ref="file">
    <button @click="sentToBackend">отправить на бэк</button>
  </div>
  <div v-if="posts.length > 0">
    <div v-for="(post, index) in posts" :key="index">
      <img :src="post.picture" alt="Post Image"/>
      <p>{{ post.text + " " + post.id }}</p>
      <p>
        <button @click="deletePost"> Удалить пост {{ post.id }}</button>
      </p>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            posts: [],
            text: '',
        };
    },
    mounted() {
        this.getPosts();
    },
    methods: {
        async getPosts() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/test-task/');
                console.log(response)
                this.posts = response.data; // Store all posts in the array
            } catch (error) {
                console.error(error);
            }
        },
        async deletePost() {
            try {
                const response = await axios.delete('\'http://127.0.0.1:8000/api/test-task/')
            } catch (error) {
                console.error(error)
            }
        },
        async sentToBackend() {
            const file = this.$refs.file.files[0];
            const reader = new FileReader();
            reader.onload = e => {
                const base64Data = reader.result;
                axios.post('http://127.0.0.1:8000/api/test-task/', {
                    text: this.text,
                    picture: base64Data
                });
            };
            const blob = new Blob([file], {type: file.type});
            reader.readAsDataURL(blob);
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
