import axios from "axios"
import { GET_EMAILS } from "./types";

export const getAllEmails = () => (dispatch) => {
  axios.get("/api/emails").then(response => {
    dispatch({
      type: GET_EMAILS,
      payload: response.data
    })
  }).catch()
};