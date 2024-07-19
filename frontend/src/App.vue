<template>
  <div class="app">
    <form class="input">
      <textarea id="random-id" cols="80" rows="16"
                placeholder="Введите текст" v-model="text">
    </textarea>
      <input class="photo_button" type="file" ref="file">
      <button class="post_button" @click="sentToBackend">отправить на бэк</button>
    </form>
      <div v-if="posts.length > 0">
    <div class="get_list" v-for="(post, index) in posts" :key="index">
      <img :src="post.picture" alt="Post Image"/>
      <p>{{ post.text }}</p>
      <p>
        <button @click="deletePost(post.id)" id="del-button"> Удалить пост</button>
      </p>
    </div>
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
                this.posts = response.data;
            } catch (error) {
                console.error(error);
            }
        },
        async deletePost(post_id) {
            try {
                const response = await axios.delete(`http://127.0.0.1:8000/api/test-task/${post_id}/`);
                await this.getPosts();
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
            await this.getPosts()
        }
    }
}
</script>

<style>
.input {
    width: 60%;
    /*margin: 10px;*/
    padding-left: 430px;
}
form {
    display: flex;
    flex-direction: column;
}
.photo_button {
    margin-top: 10px;
    align-self: flex-start;
    background: none;

}
.post_button {
    margin-top: 10px;
    align-self: center;
    background: antiquewhite;
}
.app {
    margin: 20px;
    padding: 105px;
    border: 3px solid teal;
}

.get_list {
    margin: 30px;
    padding: 15px;
    border: 3px solid teal;
}
</style>
