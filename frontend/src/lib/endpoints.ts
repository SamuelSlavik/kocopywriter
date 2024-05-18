export class Endpoints {
  private static readonly baseUrl = "http://localhost:8000/api"; // Replace with your base URL

  // USER / ADMIN --------------------------------------------------------
  static get login(): string {
    return `${Endpoints.baseUrl}/user/login`;
  }
  static get logout(): string {
    return `${Endpoints.baseUrl}/user/logout`;
  }
  static updateUser(id: string): string {
    return `${Endpoints.baseUrl}/user/update/${id}`;
  }
  static retrieveUser(id: string): string {
    return `${Endpoints.baseUrl}/user/retrieve/${id}`;
  }
  static get retrieveCurrentUser(): string {
    return `${Endpoints.baseUrl}/user/`;
  }
  static get updateUserEmail(): string {
    return `${Endpoints.baseUrl}/user/update/email/`;
  }
  static get updateUserPassword(): string {
    return `${Endpoints.baseUrl}/user/update/password`;
  }

  // HEADLINE ------------------------------------------------------------
  static get getHeadline(): string {
    return `${Endpoints.baseUrl}/headline`;
  }
  static get updateHeadline(): string {
    return `${Endpoints.baseUrl}/headline/update`;
  }


  // PRICING -------------------------------------------------------------
  static get getPriceListItems(): string {
    return `${Endpoints.baseUrl}/pricing`;
  }
  static getPriceListItem(id: string): string {
    return `${Endpoints.baseUrl}/pricing/${id}`;
  }
  static get createPriceListItem(): string {
    return `${Endpoints.baseUrl}/pricing/create`;
  }
  static updatePriceListItem(id: string): string {
    return `${Endpoints.baseUrl}/pricing/update/${id}`;
  }
  static deletePriceListItem(id: string): string {
    return `${Endpoints.baseUrl}/pricing/delete/${id}`;
  }

  // POSTS ---------------------------------------------------------------
  static get getPosts(): string {
    return `${Endpoints.baseUrl}/posts`;
  }
  static get getLatestPost(): string {
    return `${Endpoints.baseUrl}/posts/latest`;
  }
  static get getNextToLatestPosts(): string {
    return `${Endpoints.baseUrl}/posts/next-to-latest`;
  }
  static getPost(id: string): string {
    return `${Endpoints.baseUrl}/posts/${id}`;
  }
  static get createPost(): string {
    return `${Endpoints.baseUrl}/posts/create`;
  }
  static updatePost(id: string): string {
    return `${Endpoints.baseUrl}/posts/update/${id}`;
  }
  static deletePost(id: string): string {
    return `${Endpoints.baseUrl}/posts/delete/${id}`;
  }

  // IMAGES --------------------------------------------------------------
  static getImages(query?: string): string {
    return `${Endpoints.baseUrl}/images/?query=${query}`;
  }
  static getImage(id: string): string {
    return `${Endpoints.baseUrl}/images/${id}`;
  }
  static get createImage(): string {
    return `${Endpoints.baseUrl}/images/create`;
  }
  static updateImage(id: string): string {
    return `${Endpoints.baseUrl}/images/update/${id}`;
  }
  static deleteImage(id: string): string {
    return `${Endpoints.baseUrl}/images/delete/${id}`;
  }

  // REFERENCES ----------------------------------------------------------
  static get getReferences(): string {
    return `${Endpoints.baseUrl}/references`;
  }
  static getReference(id: string): string {
    return `${Endpoints.baseUrl}/references/${id}`;
  }
  static get createReference(): string {
    return `${Endpoints.baseUrl}/references/create`;
  }
  static updateReference(id: string): string {
    return `${Endpoints.baseUrl}/references/update/${id}`;
  }
  static deleteReference(id: string): string {
    return `${Endpoints.baseUrl}/references/delete/${id}`;
  }

  // BRANDS --------------------------------------------------------------
  static get getBrands(): string {
    return `${Endpoints.baseUrl}/brands`;
  }
  static getBrand(id: string): string {
    return `${Endpoints.baseUrl}/brands/${id}`;
  }
  static get createBrand(): string {
    return `${Endpoints.baseUrl}/brands/create`;
  }
  static updateBrand(id: string): string {
    return `${Endpoints.baseUrl}/brands/update/${id}`;
  }
  static deleteBrand(id: string): string {
    return `${Endpoints.baseUrl}/brands/delete/${id}`;
  }
}