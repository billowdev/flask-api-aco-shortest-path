import { UserData } from "./user.model";

// export interface SignIn {
//   token: string;
//   user: UserData;
// }

// export interface SignUp {
//   token: string;
//   user: UserData;
// }

// export interface GetSession {
//   id: string;
//   username: string;
//   token: string;
//   iat?: number;
//   exp?: number;
// }


export interface LoginData {
  user: UserLogin
}

export interface UserLogin {
  access_token: string
  email: string
  refresh_token: string
  role: string
  username: string
}
