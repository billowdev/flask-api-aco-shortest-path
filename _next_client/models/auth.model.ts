import { UserData } from "./user.model";

export interface SignIn {
  token: string;
  user: UserData;
}

// export interface SignUp {
//   token: string;
//   user: UserData;
// }

export interface GetSessionResponse {
  message: string
  paylload: SessionPayload
}

export interface SessionPayload {
  access_token: string
}


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
