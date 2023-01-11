export interface InputFieldData {
  value: string;
  errorMessage: string;
  suceedMessage: string;
}

export interface RegisterData {
  email: InputFieldData;
  password: InputFieldData;
  agreed: InputFieldData;
}
