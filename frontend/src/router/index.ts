import { createRouter, createWebHistory } from 'vue-router'
const Homepage = () => import('@/pages/sections/Homepage.vue');
const OnePage = () => import('@/pages/OnePage.vue');
const Login = () => import('@/pages/user/Login.vue');
const Profile = () => import('@/pages/user/Profile.vue');
const EditHeadline = () => import('@/pages/user/admin/EditHeadline.vue');
const Admin = () => import('@/pages/user/Admin.vue');
const Blog = () => import('@/pages/blog/Blog.vue');
const Pricing = () => import('@/pages/pricing/Pricing.vue');
const CreatePost = () => import('@/pages/user/admin/CreatePost.vue');
const CreatePriceListItem = () => import('@/pages/user/admin/CreatePriceListItem.vue');
const EditProfile = () => import('@/pages/user/admin/EditProfile.vue');
const ManageImages = () => import('@/pages/user/admin/ManageImages.vue');
const EditImage = () => import('@/pages/user/admin/EditImage.vue');
const CreateImage = () => import('@/pages/user/admin/CreateImage.vue');
const ManageBrands = () => import('@/pages/user/admin/ManageBrands.vue');
const CreateBrand = () => import('@/pages/user/admin/CreateBrand.vue');
const EditBrand = () => import('@/pages/user/admin/EditBrand.vue');
const ManagePriceListItems = () => import('@/pages/user/admin/ManagePriceListItems.vue');
const EditPriceListItem = () => import('@/pages/user/admin/EditPriceListItem.vue');
const ManageReferences = () => import('@/pages/user/admin/ManageReferences.vue');
const CreateReference = () => import('@/pages/user/admin/CreateReference.vue');
const EditReference = () => import('@/pages/user/admin/EditReference.vue');
const ManagePosts = () => import('@/pages/user/admin/ManagePosts.vue');
const EditPost = () => import('@/pages/user/admin/EditPost.vue');
const DetailImage = () => import('@/pages/user/admin/DetailImage.vue');
const DetailBrand = () => import('@/pages/user/admin/DetailBrand.vue');
const DetailPriceListItem = () => import('@/pages/user/admin/DetailPriceListItem.vue');
const DetailReference = () => import('@/pages/user/admin/DetailReference.vue');
const DetailPost = () => import('@/pages/user/admin/DetailPost.vue');
const Post = () => import('@/pages/blog/Post.vue');

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
      component: Homepage,
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
