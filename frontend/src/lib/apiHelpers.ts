import type {
  Brand,
  Credentials,
  Headline,
  Image,
  NewPost,
  NewPriceListItem, Post,
  PriceListItem, Reference,
  Token,
  User
} from "@/lib/models";
import {Endpoints} from "@/lib/endpoints";
import axios from "axios";
import type {AxiosResponse} from "axios";

const getHeaders = () => {
  return { headers: { "Authorization": "Bearer " + localStorage.getItem("token") }}
}
const getHeadersWithFile = () => {
  return {
    headers: {
      "Authorization": "Bearer " + localStorage.getItem("token"),
      'Content-Type': 'multipart/form-data',
    }
  }
}

// USER ------------------------------------------------------------------------------------
export class userApi {
  static async login(credentials: Credentials) : Promise<AxiosResponse<Token, Token>>  {
    return await axios.post(
      Endpoints.login,
      credentials,
      getHeaders()
    )
  }
  static async retrieveCurrentUser() : Promise<AxiosResponse<User, User>> {
    return await axios.get(
      Endpoints.retrieveCurrentUser,
      getHeaders()
    )
  }
  static async updateEmail(email: string) : Promise<AxiosResponse<User, User>> {
    return await axios.put(
      Endpoints.updateUserEmail,
      {email: email},
      getHeaders()
    )
  }
  static async updatePassword(password: string) : Promise<AxiosResponse<User, User>> {
    return await axios.put(
      Endpoints.updateUserPassword,
      {password: password},
      getHeaders()
    )
  }
}

// HEADLINE ------------------------------------------------------------------------------------
export class headlineApi {
  static async getHeadline(): Promise<AxiosResponse<Headline, any>> {
    return await axios.get(
      Endpoints.getHeadline,
      getHeaders()
    )
  }
  static async updateHeadline(newHeadline: Headline): Promise<AxiosResponse<Headline, any>> {
    return await axios.put(
      Endpoints.updateHeadline,
      newHeadline,
      getHeaders()
    )
  }
}

// PRICING ------------------------------------------------------------------------------------
export class pricingApi {
  static async getPriceListItems(): Promise<AxiosResponse<PriceListItem[], any>> {
    return await axios.get(
      Endpoints.getPriceListItems,
      getHeaders()
    )
  }
  static async getPriceListItem(id: string): Promise<AxiosResponse<PriceListItem, any>> {
    return await axios.get(
      Endpoints.getPriceListItem(id),
      getHeaders()
    )
  }
  static async createPriceListItem(newItem: NewPriceListItem): Promise<AxiosResponse<PriceListItem, any>> {
    return await axios.post(
      Endpoints.createPriceListItem,
      newItem,
      getHeaders()
    )
  }
  static async updatePriceListItem(id: string, newItem: NewPriceListItem): Promise<AxiosResponse<PriceListItem, any>> {
    return await axios.put(
      Endpoints.updatePriceListItem(id),
      newItem,
      getHeaders()
    )
  }
  static async deletePriceListItem(id: string): Promise<AxiosResponse<PriceListItem, any>> {
    return await axios.delete(
      Endpoints.deletePriceListItem(id),
      getHeaders()
    )
  }
}

// IMAGES ------------------------------------------------------------------------------------
export class imagesApi {
  static async getImages(query?: string): Promise<AxiosResponse<Image[], any>> {
    return await axios.get(
      Endpoints.getImages(query),
      getHeaders()
    )
  }
  static async getImage(id: string): Promise<AxiosResponse<Image, any>> {
    return await axios.get(
      Endpoints.getImage(id),
      getHeaders()
    )
  }
  static async createImage(formData: FormData): Promise<AxiosResponse<any>> {
    return axios.post(
      Endpoints.createImage,
      formData,
      getHeadersWithFile()
    );
  }
  static async updateImage(id: string, formData: FormData): Promise<AxiosResponse<Image, any>> {
    return await axios.put(
      Endpoints.updateImage(id),
      formData,
      getHeadersWithFile()
    )
  }
  static async deleteImage(id: string): Promise<AxiosResponse<Image, any>> {
    return await axios.delete(
      Endpoints.deleteImage(id),
      getHeaders()
    )
  }
}

// BRANDS ------------------------------------------------------------------------------------
export class brandsApi {
  static async getBrands(): Promise<AxiosResponse<Brand[], any>> {
    return await axios.get(
      Endpoints.getBrands,
      getHeaders()
    )
  }
  static async getBrand(id: string): Promise<AxiosResponse<Brand, any>> {
    return await axios.get(
      Endpoints.getBrand(id),
      getHeaders()
    )
  }
  static async createBrand(formData: FormData): Promise<AxiosResponse<Brand, any>> {
    return axios.post(
      Endpoints.createBrand,
      formData,
      getHeadersWithFile()
    );
  }
  static async updateBrand(id: string, formData: FormData): Promise<AxiosResponse<Brand, any>> {
    return await axios.put(
      Endpoints.updateBrand(id),
      formData,
      getHeadersWithFile()
    )
  }
  static async deleteBrand(id: string): Promise<AxiosResponse<Brand, any>> {
    return await axios.delete(
      Endpoints.deleteBrand(id),
      getHeaders()
    )
  }
}

// REFERENCES ------------------------------------------------------------------------------------
export class referencesApi {
  static async getReferences(): Promise<AxiosResponse<Reference[], any>> {
    return await axios.get(
      Endpoints.getReferences,
      getHeaders()
    )
  }
  static async getReference(id: string): Promise<AxiosResponse<Reference, any>> {
    return await axios.get(
      Endpoints.getReference(id),
      getHeaders()
    )
  }
  static async createReference(formData: FormData): Promise<AxiosResponse<Reference, any>> {
    return axios.post(
      Endpoints.createReference,
      formData,
      getHeadersWithFile()
    );
  }
  static async updateReference(id: string, formData: FormData): Promise<AxiosResponse<Reference, any>> {
    return await axios.put(
      Endpoints.updateReference(id),
      formData,
      getHeadersWithFile()
    )
  }
  static async deleteReference(id: string): Promise<AxiosResponse<Reference, any>> {
    return await axios.delete(
      Endpoints.deleteReference(id),
      getHeaders()
    )
  }
}

// POSTS ------------------------------------------------------------------------------------
export class postsApi {
  static async getPosts(): Promise<AxiosResponse<Post[], any>> {
    return await axios.get(
      Endpoints.getPosts,
      getHeaders()
    )
  }
  static async getPost(id: string): Promise<AxiosResponse<Post, any>> {
    return await axios.get(
      Endpoints.getPost(id),
      getHeaders()
    )
  }
  static async createPost(post: NewPost): Promise<AxiosResponse<Post, any>> {
    return axios.post(
      Endpoints.createPost,
      post,
      getHeaders()
    );
  }
  static async updatePost(id: string, post: NewPost): Promise<AxiosResponse<Post, any>> {
    return await axios.put(
      Endpoints.updatePost(id),
      post,
      getHeaders()
    )
  }
  static async deletePost(id: string): Promise<AxiosResponse<Post, any>> {
    return await axios.delete(
      Endpoints.deletePost(id),
      getHeaders()
    )
  }
}
