import { createRouter, createWebHistory } from 'vue-router'
import Homepage from '@/pages/sections/Homepage.vue';
import OnePage from '@/pages/OnePage.vue';
import Login from '@/pages/user/Login.vue';
import Profile from '@/pages/user/Profile.vue';
import EditHeadline from '@/pages/user/admin/EditHeadline.vue';
import Admin from '@/pages/user/Admin.vue';
import Blog from '@/pages/blog/Blog.vue';
import Pricing from '@/pages/pricing/Pricing.vue';
import CreatePost from '@/pages/user/admin/CreatePost.vue';
import CreatePriceListItem from '@/pages/user/admin/CreatePriceListItem.vue';
import EditProfile from '@/pages/user/admin/EditProfile.vue';
import ManageImages from '@/pages/user/admin/ManageImages.vue';
import EditImage from '@/pages/user/admin/EditImage.vue';
import CreateImage from '@/pages/user/admin/CreateImage.vue';
import ManageBrands from '@/pages/user/admin/ManageBrands.vue';
import CreateBrand from '@/pages/user/admin/CreateBrand.vue';
import EditBrand from '@/pages/user/admin/EditBrand.vue';
import ManagePriceListItems from '@/pages/user/admin/ManagePriceListItems.vue';
import EditPriceListItem from '@/pages/user/admin/EditPriceListItem.vue';
import ManageReferences from '@/pages/user/admin/ManageReferences.vue';
import CreateReference from '@/pages/user/admin/CreateReference.vue';
import EditReference from '@/pages/user/admin/EditReference.vue';
import ManagePosts from '@/pages/user/admin/ManagePosts.vue';
import EditPost from '@/pages/user/admin/EditPost.vue';
import DetailImage from '@/pages/user/admin/DetailImage.vue';
import DetailBrand from '@/pages/user/admin/DetailBrand.vue';
import DetailPriceListItem from '@/pages/user/admin/DetailPriceListItem.vue';
import DetailReference from '@/pages/user/admin/DetailReference.vue';
import DetailPost from '@/pages/user/admin/DetailPost.vue';
import Post from '@/pages/blog/Post.vue';
import ErrorPage from '@/pages/404.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, SavedPosition) {
    if (to.hash) {
      const el = window.location.href.split("#")[1];
      if (el.length) {
        document.getElementById(el)?.scrollIntoView({ behavior: "smooth" });
      }
    } else if (SavedPosition) {
      return SavedPosition;
    } else {
      document.getElementById("app")?.scrollIntoView({ behavior: "smooth" });
    }
  },
  routes: [
    {
      path: "/:notFound",
      component: ErrorPage,
    },
    {
      path: '/',
      name: 'home',
      component: OnePage
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/admin',
      name: 'admin',
      component: Admin,
      children: [
        {
          path: ":notFound",
          component: Profile,
        },
        {
          path: '',
          component: Profile
        },
        {
          path: "profile/edit",
          component: EditProfile
        },
        // HEADLINE
        {
          path: 'headline/edit',
          component: EditHeadline
        },

        // IMAGES
        {
          path: "images",
          component: ManageImages
        },
        {
          path: "images/create",
          component: CreateImage
        },
        {
          path: "images/edit/:id",
          component: EditImage
        },
        {
          path: "images/detail/:id",
          component: DetailImage
        },

        // BRAND
        {
          path: "brands",
          component: ManageBrands
        },
        {
          path: "brands/create",
          component: CreateBrand
        },
        {
          path: "brands/edit/:id",
          component: EditBrand
        },
        {
          path: "brands/detail/:id",
          component: DetailBrand
        },
        // PRICE LIST ITEMS
        {
          path: "pricing",
          component: ManagePriceListItems
        },
        {
          path: "pricing/create",
          component: CreatePriceListItem
        },
        {
          path: "pricing/edit/:id",
          component: EditPriceListItem
        },
        {
          path: "pricing/detail/:id",
          component: DetailPriceListItem
        },
        // REFERENCES
        {
          path: "references",
          component: ManageReferences
        },
        {
          path: "references/create",
          component: CreateReference
        },
        {
          path: "references/edit/:id",
          component: EditReference
        },
        {
          path: "references/detail/:id",
          component: DetailReference
        },
        // POSTS
        {
          path: "posts",
          component: ManagePosts
        },
        {
          path: "posts/create",
          component: CreatePost
        },
        {
          path: "posts/edit/:id",
          component: EditPost
        },
        {
          path: "posts/detail/:id",
          component: DetailPost
        },
      ]
    },
    {
      path: "/pricing",
      component: Pricing
    },
    {
      path: "/blog",
      component: Blog
    },
    {
      path: "/blog/:id",
      component: Post
    }
  ]
})



export default router
