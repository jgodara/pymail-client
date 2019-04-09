import { GET_EMAILS } from "../actions/types";

const initialState = {
  emails: []
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_EMAILS:
      return {
        ...state,
        emails: action.payload.emails
      };
    default:
      return initialState
  }
}