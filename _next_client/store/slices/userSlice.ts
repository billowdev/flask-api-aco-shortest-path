import { createSlice, createAsyncThunk, PayloadAction } from "@reduxjs/toolkit";
import { UserData } from "@/models/user.model";
import { RootState } from "@/store/store";
import * as authService from "@/services/authService";
import httpClient from "@/utils/httpClient.util";
import { AxiosRequestConfig } from "axios";
import Router from "next/router";

interface UserState {
	accessToken: string;
	isAuthenticated: boolean;
	isAuthenticating: boolean;
	user?: UserData;
}


const initialState: UserState = {
	accessToken: "",
	isAuthenticated: false,
	isAuthenticating: true,
	user: undefined,
};

interface SignAction {
	username: string;
	password: string;
}


export const signIn = createAsyncThunk(
	"user/signin",
	async (credential: SignAction) => {
		const response = await authService.signIn(credential);
		if (response.user == null) {
			throw new Error("login failed");
		}

		httpClient.interceptors.request.use((config?: any) => {
			if (config && config.headers) {
				config.headers["Authorization"] = `Bearer ${response.token}`;
			}

			return config;
		});
		return response;
	}
);

export const signOut = createAsyncThunk("user/signout", async () => {
	await authService.signOut();
	Router.push("/panel/login");
});

export const getSession = createAsyncThunk("user/fetchSession", async () => {
	const response = await authService.getSession();
	// set access token
	if (response) {
		httpClient.interceptors.request.use((config?: any) => {
			if (config && config.headers) {
				config.headers["Authorization"] = `Bearer ${response.access_token}`;
			}
			return config;
		});
	}
	return response;
});

const userSlice = createSlice({
	name: "user",
	initialState: initialState,
	reducers: {
	},
	extraReducers: (builder) => {
		builder.addCase(signIn.fulfilled, (state, action) => {
			state.isAuthenticated = true;
			state.isAuthenticating = false;
			state.user = action.payload.user;
		});
		builder.addCase(signIn.rejected, (state, action) => {
			state.isAuthenticated = false;
			state.isAuthenticating = false;
			state.user = undefined;
		});
		builder.addCase(signOut.fulfilled, (state, action) => {
			state.accessToken = "";
			state.isAuthenticated = false;
			state.isAuthenticating = false;
			state.user = undefined;
		});
		builder.addCase(getSession.fulfilled, (state, action) => {
			state.isAuthenticating = false;
			if (action.payload) {
				state.accessToken = action.payload.access_token
				state.isAuthenticated = true;
			}
		});
		builder.addCase(getSession.rejected, (state, action) => {
			state.isAuthenticating = true;
			state.isAuthenticated = false;
			state.accessToken = ""
			state.user = undefined;
		});
	},
});

export const userSelector = (store: RootState) => store.user;
export const isAuthenticatedSelector = (store: RootState): boolean =>
	store.user.isAuthenticated;
export const isAuthenticatingSelector = (store: RootState): boolean =>
	store.user.isAuthenticating;


// // export reducer
export default userSlice.reducer;
