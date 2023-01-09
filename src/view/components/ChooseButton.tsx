import React from "react";
import { Link } from "react-router-dom";

export default class ChooseButton extends React.Component {

    render() {
        console.warn(this.
        public get value() : string {
            return this._value;
        }
        public set value(v : string) {
            this._value = v;
        }
        
        return <Link to="/">
            <button className="Button">{this.props.name}}</button>
        </Link>;
    }
};