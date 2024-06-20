<script setup lang="ts">
import {inject, onMounted, ref} from "vue";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user-store";
import {EditorContent, useEditor} from "@tiptap/vue-3";
import StarterKit from "@tiptap/starter-kit";
import {Paragraph} from "@tiptap/extension-paragraph";
import {Heading} from "@tiptap/extension-heading";
import {BulletList} from "@tiptap/extension-bullet-list";
import { TextStyle } from "@tiptap/extension-text-style";
// @ts-ignore
import { Color } from '@tiptap/extension-color';
import {Image} from "@tiptap/extension-image";
import {Link} from "@tiptap/extension-link";
import {TextAlign} from "@tiptap/extension-text-align";
import type {NewPost} from "@/lib/models";
import {postsApi} from "@/lib/apiHelpers";

const loading = ref<boolean>(false)
const user = useUserStore()
const router = useRouter()
const notificationStore: any = inject('notificationStore')

const postId = router.currentRoute.value.params.id.toString() || ""

const newPost = ref<NewPost>(
    {
      title: "",
      short: "",
      image: "",
      content: "",
      date: "",
    }
)

const editor = useEditor({
  content: newPost.value.content,
  extensions: [
    StarterKit,
    Paragraph,
    Heading,
    BulletList,
    Image,
    TextStyle,
    Color,
    Link.configure({
      HTMLAttributes: {
        // Change rel to different value
        // Allow search engines to follow links(remove nofollow)
        rel: 'noopener noreferrer',
        // Remove target entirely so links open in current tab
        target: "_blank",
      },
    }),
    TextAlign.configure({
      types: ['heading', 'paragraph'],
    }),
  ],
  onUpdate({ editor }) {
    newPost.value.content = editor.getHTML()
  },
})


const addImageToEditor = (editor: any) => {
  const url = window.prompt('URL')

  if (url && editor) {
    editor.chain().focus().setImage({ src: url }).run()
  }
}
const addLinkToEditor = (editor: any) => {
  const previousUrl = editor.getAttributes('link').href
  const url = window.prompt('URL', previousUrl)

  if (url === null) {
    return
  }
  if (url === '') {
    editor.chain().focus().extendMarkRange('link').unsetLink().run()
    return
  }
  editor.chain().focus().extendMarkRange('link').setLink({ href: url }).run()
}

const toggleOrangeTextColor = (editor: any) => {
  const currentColor = editor.getAttributes('textStyle').color
  if (currentColor === 'rgb(209, 119, 61)') {
    editor.chain().focus().unsetColor().run()
  } else {
    editor.chain().focus().setColor('rgb(209, 119, 61)').run()
  }
}

const submitPost = async () => {
  try {
    const response = await postsApi.updatePost(postId, newPost.value)
    if (response.status === 200) {
      notificationStore.addNotification({ type: "success", message: "Post updated successfully" });
      await router.push('/admin/posts');
    } else {
      notificationStore.addNotification({ type: "error", message: `Failed to update post: ${response.statusText}` });
    }
  } catch (error: any) {
    notificationStore.addNotification({ type: "error", message: `Failed to update post: ${error.response.data.detail}` })
  }
}

const loadPost = async () => {
  try {
    loading.value = true
    const response = await postsApi.getPost(postId)
    newPost.value.title = response.data.title
    newPost.value.short = response.data.short
    newPost.value.image = response.data.image
    newPost.value.date = response.data.date
    newPost.value.content = response.data.content
    editor.value?.commands.setContent(newPost.value.content)
  } catch (e: any) {
    notificationStore.addNotification({
      type: 'error',
      message: 'Failed to load post: ' + e.response.data.detail,
    })
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadPost()
})

</script>

<template>
  <Container>
    <h2>Edit Post</h2>
    <br/>
    <p>To insert images into the post, insert its url, e.g.: https://kocopywriter.cz/images/posts/image1.png</p>
    <p>
      You can save those images through <router-link to="/admin/images">Manage images</router-link>,
      or you can you use cloud/drive.
    </p>
    <Loader v-if="loading"/>
    <div class="form-block" v-else v-if="newPost">
      <form @submit.prevent="submitPost">
        <div>
          <label for="title">Title</label>
          <input
              type="text"
              name="title"
              placeholder="Title"
              v-model="newPost.title"
              required

          />
        </div>
        <div>
          <label for="title">Date</label>
          <input
              type="date"
              name="date"
              placeholder="Date"
              v-model="newPost.date"
              required
          />
        </div>
        <div>
          <label for="title">Image url / Thumbnail</label>
          <input
              type="text"
              name="image"
              placeholder="Image url"
              v-model="newPost.image"
          />
        </div>

        <div>
          <label for="short">Short</label>
          <textarea
              name="short"
              placeholder="Short"
              required
              v-model="newPost.short"
          />
        </div>

        <div>
          <label>Content</label>

          <div class="tiptap-toolbar" v-if="editor">
            <button
                type="button"
                @click="editor.chain().focus().setParagraph().run()" :class="{ 'is-active': editor.isActive('paragraph') }"
            >
              p
            </button>
            <button
                type="button"
                @click="editor.chain().focus().toggleHeading({ level: 1 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }"
            >
              h1
            </button>
            <button
                type="button"
                @click="editor.chain().focus().toggleHeading({ level: 2 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }"
            >
              h2
            </button>
            <button
                type="button"
                @click="editor.chain().focus().toggleHeading({ level: 3 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }"
            >
              h3
            </button>
            <button
                type="button"
                @click="editor.chain().focus().toggleHeading({ level: 4 }).run()" :class="{ 'is-active': editor.isActive('heading', { level: 4 }) }"
            >
              h4
            </button>

            <div></div>

            <button
                type="button"
                @click="editor.chain().focus().toggleBold().run()" :disabled="!editor.can().chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }"
            >
              <b>b</b>
            </button>
            <button
                type="button"
                @click="editor.chain().focus().toggleItalic().run()" :disabled="!editor.can().chain().focus().toggleItalic().run()" :class="{ 'is-active': editor.isActive('italic') }"
            >
              <i>i</i>
            </button>
            <button
                type="button"
                @click="toggleOrangeTextColor(editor)" :class="{ 'is-active': editor.isActive({ color: 'rgb(209, 119, 61)' }) }"
            >
              <b><span style="color: rgb(209, 119, 61)">A</span></b>
            </button>

            <div></div>

            <button
                type="button"
                @click="editor.chain().focus().setTextAlign('left').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'left' }) }"
            >
              Left
            </button>
            <button
                type="button"
                @click="editor.chain().focus().setTextAlign('center').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'center' }) }"
            >
              Center
            </button>
            <button
                type="button"
                @click="editor.chain().focus().setTextAlign('right').run()" :class="{ 'is-active': editor.isActive({ textAlign: 'right' }) }"
            >
              Right
            </button>

            <div></div>

            <button
                type="button"
                @click="() => addImageToEditor(editor)"
            >
              Image
            </button>
            <button
                type="button"
                @click="() => addLinkToEditor(editor)"
            >
              Link
            </button>

            <div></div>

            <button
                type="button"
                @click="editor.chain().focus().toggleBulletList().run()" :class="{ 'is-active': editor.isActive('bulletList') }"
            >
              Unordered List
            </button>
            <button
                type="button"
                @click="editor.chain().focus().toggleOrderedList().run()" :class="{ 'is-active': editor.isActive('orderedList') }"
            >
              Ordered List
            </button>

          </div>
          <editor-content :editor="editor">
          </editor-content>
        </div>
        <br/>
        <button
            class="button"
            type="submit"
        >Update post</button>
      </form>
    </div>

    <div class="hr"></div>
    <div v-html="newPost.content">
    </div>
  </Container>
</template>

<style>

</style>