export class Endpoints {
  private static readonly baseUrl = "http://localhost:8000/api"; // Replace with your base URL

  // USER / ADMIN
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
    return `${Endpoints.baseUrl}/user`;
  }


  // PRICING


  // POSTS


}